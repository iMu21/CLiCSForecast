from datetime import timedelta
from dateutil.relativedelta import relativedelta
from forecasts.constants import Constants, ProcessStatus
from forecasts.models.enroll import Enroll
from forecasts.models.enroll_inactive_cycle import EnrollInactiveCycle
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.group_policy_cluster_inactive_cycle import GroupPolicyClusterInactiveCycle
from forecasts.models.group_policy_inactive_cycle import GroupPolicyInactiveCycle
from forecasts.services.inactive_cycle_service import is_inactive_on_date

def update_enroll_statistics():
    if Constants.ENROLL_PROCESS_STATUS == ProcessStatus.AVAILABLE:
        Constants.ENROLL_PROCESS_STATUS = ProcessStatus.PROCESSING
        print("Enroll statistics process start for page  "+ str(Constants.ENROLL_RUNNING_PAGE))
    else:
        return
    
    to_id = Constants.ENROLL_BATCH_SIZE * Constants.ENROLL_RUNNING_PAGE
    from_id = (Constants.ENROLL_BATCH_SIZE * (Constants.ENROLL_RUNNING_PAGE+1))-1
    current_month_start_date = Constants.REPORT_START_DATE.replace(day=1)
    current_month_end_date = (Constants.REPORT_START_DATE + relativedelta(months=1)) - timedelta(days=1)

    one_month = timedelta(days=31)
    one_day = timedelta(days=1)

    enrolls = Enroll.objects.filter(clics_db_id__lt=from_id,clics_db_id__gt = to_id)
    sorted_inactive_cycles = EnrollInactiveCycle.objects.filter(parent_id__lt=from_id,parent_id__gt = to_id).order_by('parent_id','start_date','end_date')
    sorted_group_policy_inactive_cycles = GroupPolicyInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_cluster_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')

    while current_month_end_date <= Constants.REPORT_END_DATE:
        total_inactive_weight = int(0)
        total_active_weight = int(0)
        total_active_at_least_one_day = int(0)
        enroll_active_old_age_weight = int(0)
        enroll_inactive_old_age_weight = int(0)
        enroll_active_mid_age_weight = int(0)
        enroll_inactive_mid_age_weight = int(0)
        enroll_active_young_age_weight = int(0)
        enroll_inactive_young_age_weight = int(0)
        enroll_active_child_age_weight = int(0)
        enroll_inactive_child_age_weight = int(0)
        for enroll in enrolls:
            date = current_month_start_date
            is_active_in_month = False
            while date <= current_month_end_date:
                if enroll.effective_date <= date:
                    age = calculate_age(date,enroll.birth_date)
                    if (is_inactive_on_date(sorted_group_policy_inactive_cycles,enroll.group_policy_id,date)) or ( 
                        is_inactive_on_date(sorted_group_policy_cluster_inactive_cycles,enroll.group_policy_cluster_id,date))or ( 
                        is_inactive_on_date(sorted_inactive_cycles,enroll.clics_db_id,date)):
                        total_inactive_weight+=1
                        if age<=18:
                            enroll_inactive_child_age_weight+=1
                        elif age<=30:
                            enroll_inactive_young_age_weight+=1
                        elif age<=55:
                            enroll_inactive_mid_age_weight+=1
                        else:
                            enroll_inactive_old_age_weight+=1
                    else:
                        total_active_weight+=1
                        if age<=18:
                            enroll_active_child_age_weight+=1
                        elif age<=30:
                            enroll_active_young_age_weight+=1
                        elif age<=55:
                            enroll_active_mid_age_weight+=1
                        else:
                            enroll_active_old_age_weight+=1
                        is_active_in_month = True
                date = date + one_day
            if is_active_in_month:
                total_active_at_least_one_day+=1

        year = current_month_start_date.year
        month = current_month_start_date.month
        
        reports = DataAnalaysisReportClaimForecast.objects.filter(year=year,month=month)
        report = None
        if len(reports) > 0:
            report = reports[0]
            if Constants.ENROLL_RUNNING_PAGE == 0:
                report.enroll_active_weight = 0
                report.enroll_inactive_weight = 0
                report.enroll_active_at_least_one_day = 0
                report.enroll_active_child_age_weight = 0
                report.enroll_active_young_age_weight = 0
                report.enroll_active_mid_age_weight = 0
                report.enroll_active_old_age_weight = 0
                report.enroll_inactive_child_age_weight = 0
                report.enroll_inactive_young_age_weight = 0
                report.enroll_inactive_mid_age_weight = 0
                report.enroll_inactive_old_age_weight = 0
        else:
            report = DataAnalaysisReportClaimForecast()
            report.year=year
            report.month = month

        report.enroll_active_weight += total_active_weight
        report.enroll_inactive_weight += total_inactive_weight
        report.enroll_active_at_least_one_day += total_active_at_least_one_day
        report.enroll_active_child_age_weight += enroll_active_child_age_weight
        report.enroll_active_young_age_weight += enroll_active_young_age_weight
        report.enroll_active_mid_age_weight += enroll_active_mid_age_weight
        report.enroll_active_old_age_weight += enroll_active_old_age_weight
        report.enroll_inactive_child_age_weight += enroll_inactive_child_age_weight
        report.enroll_inactive_young_age_weight += enroll_inactive_young_age_weight
        report.enroll_inactive_mid_age_weight += enroll_inactive_mid_age_weight
        report.enroll_inactive_old_age_weight += enroll_inactive_old_age_weight
        report.save()       

        current_month_start_date = (current_month_start_date+one_month).replace(day=1)
        current_month_end_date = (current_month_start_date + relativedelta(months=1)) - timedelta(days=1)
    Constants.ENROLL_RUNNING_PAGE = Constants.ENROLL_RUNNING_PAGE + 1
    if Constants.ENROLL_RUNNING_PAGE> Constants.ENROLL_MAX_PAGE_SIZE:
        Constants.ENROLL_PROCESS_STATUS = ProcessStatus.SLEEP
        print("Enroll statistics process ended for page  "+ str(Constants.ENROLL_RUNNING_PAGE-1))
        print("Process finished!. Will process after 24 hours again")
    else:
        Constants.ENROLL_PROCESS_STATUS = ProcessStatus.AVAILABLE
        print("Enroll statistics process ended for page  "+ str(Constants.ENROLL_RUNNING_PAGE-1))

def calculate_age(birth_date, date):
    delta = relativedelta(birth_date,date, birth_date)
    age = delta.years
    return age
