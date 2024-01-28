from datetime import timedelta
from dateutil.relativedelta import relativedelta
from forecasts.constants import Constants
from forecasts.models.group_policy_cluster import GroupPolicyCluster
from forecasts.models.group_policy_cluster_inactive_cycle import GroupPolicyClusterInactiveCycle
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.group_policy_inactive_cycle import GroupPolicyInactiveCycle
from forecasts.services.inactive_cycle_service import is_inactive_on_date

def update_group_policy_cluster_statistics():
    print("Group policy cluster statistics update process begin")
    current_month_start_date = Constants.REPORT_START_DATE.replace(day=1)
    current_month_end_date = (Constants.REPORT_START_DATE + relativedelta(months=1)) - timedelta(days=1)

    one_month = timedelta(days=31)
    one_day = timedelta(days=1)

    all_group_policy_clusters = GroupPolicyCluster.objects.all()
    sorted_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_inactive_cycles = GroupPolicyInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')

    while current_month_end_date <= Constants.REPORT_END_DATE:
        total_inactive_weight = int(0)
        total_active_weight = int(0)
        total_active_at_least_one_day = int(0)
        for group_policy_cluster in all_group_policy_clusters:
            date = current_month_start_date
            is_active_in_month = False
            while date <= current_month_end_date:
                if group_policy_cluster.effective_date <= date:
                    if(is_inactive_on_date(sorted_group_policy_inactive_cycles
                                                ,group_policy_cluster.group_policy_id,
                                                date)) or( 
                        is_inactive_on_date(sorted_inactive_cycles,
                                            group_policy_cluster.clics_db_id,
                                            date)):
                        total_inactive_weight+=1
                    else:
                        total_active_weight+=1
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
        else:
            report = DataAnalaysisReportClaimForecast()
            report.year=year
            report.month = month

        report.group_policy_cluster_active_weight = total_active_weight
        report.group_policy_cluster_inactive_weight = total_inactive_weight
        report.group_policy_cluster_active_at_least_one_day = total_active_at_least_one_day
        report.save()
        

        current_month_start_date = (current_month_start_date+one_month).replace(day=1)
        current_month_end_date = (current_month_start_date + relativedelta(months=1)) - timedelta(days=1)
    print("Group policy cluster statistics update process ended")
