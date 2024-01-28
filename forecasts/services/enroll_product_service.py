from datetime import timedelta
from dateutil.relativedelta import relativedelta
from forecasts.constants import Constants, ProcessStatus
from forecasts.models.enroll import Enroll
from forecasts.models.enroll_inactive_cycle import EnrollInactiveCycle
from forecasts.models.enroll_product import EnrollProduct
from forecasts.models.enroll_product_inactive_cycle import EnrollProductInactiveCycle
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.group_policy_cluster_inactive_cycle import GroupPolicyClusterInactiveCycle
from forecasts.models.group_policy_inactive_cycle import GroupPolicyInactiveCycle
from forecasts.models.product import Product
from forecasts.services.inactive_cycle_service import is_inactive_on_date

def update_enroll_product_statistics():
    if Constants.ENROLL_PRODUCT_PROCESS_STATUS == ProcessStatus.AVAILABLE:
        Constants.ENROLL_PRODUCT_PROCESS_STATUS = ProcessStatus.PROCESSING
        print("Enroll product statistics process start for page  "+ str(Constants.ENROLL_PRODUCT_RUNNING_PAGE))
    else:
        return
    
    to_id = Constants.ENROLL_PRODUCT_BATCH_SIZE * Constants.ENROLL_PRODUCT_RUNNING_PAGE
    from_id = (Constants.ENROLL_PRODUCT_BATCH_SIZE * (Constants.ENROLL_PRODUCT_RUNNING_PAGE+1))-1
    current_month_start_date = Constants.REPORT_START_DATE.replace(day=1)
    current_month_end_date = (Constants.REPORT_START_DATE + relativedelta(months=1)) - timedelta(days=1)

    one_month = timedelta(days=31)
    one_day = timedelta(days=1)

    enroll_products = EnrollProduct.objects.filter(clics_db_id__lt=from_id,clics_db_id__gt = to_id)
    sorted_inactive_cycles = EnrollProductInactiveCycle.objects.filter(parent_id__lt=from_id,parent_id__gt = to_id).order_by('parent_id','start_date','end_date')
    
    sorted_enroll_inactive_cycles = EnrollInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_inactive_cycles = GroupPolicyInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_cluster_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_cluster_product_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    
    while current_month_end_date <= Constants.REPORT_END_DATE:
        total_inactive_weight = int(0)
        total_active_weight = int(0)
        total_active_at_least_one_day = int(0)
        enroll_product_GM_active_weight = int(0)
        enroll_product_GL_active_weight = int(0)
        enroll_product_IL_active_weight = int(0)
        enroll_product_ID_active_weight = int(0)
        enroll_product_BM_active_weight = int(0)
        enroll_product_BL_active_weight = int(0)
        enroll_product_GM_inactive_weight = int(0)
        enroll_product_GL_inactive_weight = int(0)
        enroll_product_IL_inactive_weight = int(0)
        enroll_product_ID_inactive_weight = int(0)
        enroll_product_BM_inactive_weight = int(0)
        enroll_product_BL_inactive_weight = int(0)

        for enroll_product in enroll_products:
            date = current_month_start_date
            is_active_in_month = False
            while date <= current_month_end_date:
                if enroll_product.effective_date <= date:
                    product = Product.objects.get(clics_db_id= enroll_product.product_id)
                    enroll = Enroll.objects.get(clics_db_id= enroll_product.enroll_id)
                    if (is_inactive_on_date(sorted_inactive_cycles,enroll_product.clics_db_id,date)) or ( 
                        is_inactive_on_date(sorted_enroll_inactive_cycles,enroll_product.enroll_id,date))or ( 
                        is_inactive_on_date(sorted_group_policy_inactive_cycles,enroll.group_policy_id,date))or ( 
                        is_inactive_on_date(sorted_group_policy_cluster_inactive_cycles,enroll.group_policy_cluster_id,date))or ( 
                        is_inactive_on_date(sorted_group_policy_cluster_product_inactive_cycles,enroll_product.group_policy_cluster_product_id,date)):
                        total_inactive_weight+=1
                        if product == "GM":
                            enroll_product_GM_inactive_weight+=1
                        elif product == "GL":
                            enroll_product_GL_inactive_weight+=1
                        elif product == "BM":
                            enroll_product_BM_inactive_weight+=1
                        elif product == "BL":
                            enroll_product_BL_inactive_weight+=1
                        elif product == "IL":
                            enroll_product_IL_inactive_weight+=1
                        elif product == "ID":
                            enroll_product_ID_inactive_weight+=1
                    else:
                        total_active_weight+=1
                        if product == "GM":
                            enroll_product_GM_active_weight+=1
                        elif product == "GL":
                            enroll_product_GL_active_weight+=1
                        elif product == "BM":
                            enroll_product_BM_active_weight+=1
                        elif product == "BL":
                            enroll_product_BL_active_weight+=1
                        elif product == "IL":
                            enroll_product_IL_active_weight+=1
                        elif product == "ID":
                            enroll_product_ID_active_weight+=1
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
                report.enroll_product_GM_active_weight = 0
                report.enroll_product_GL_active_weight = 0
                report.enroll_product_IL_active_weight = 0
                report.enroll_product_ID_active_weight = 0
                report.enroll_product_BM_active_weight = 0
                report.enroll_product_BL_active_weight = 0
                report.enroll_product_GM_inactive_weight = 0
                report.enroll_product_GL_inactive_weight = 0
                report.enroll_product_IL_inactive_weight = 0
                report.enroll_product_ID_inactive_weight = 0
                report.enroll_product_BM_inactive_weight = 0
                report.enroll_product_BL_inactive_weight = 0
        else:
            report = DataAnalaysisReportClaimForecast()
            report.year=year
            report.month = month

        report.enroll_product_active_weight += total_active_weight
        report.enroll_product_inactive_weight += total_inactive_weight
        report.enroll_product_active_at_least_one_day += total_active_at_least_one_day
        report.enroll_product_GM_active_weight += enroll_product_GM_active_weight
        report.enroll_product_GL_active_weight += enroll_product_GL_active_weight
        report.enroll_product_IL_active_weight += enroll_product_IL_active_weight
        report.enroll_product_ID_active_weight += enroll_product_ID_active_weight
        report.enroll_product_BM_active_weight += enroll_product_BM_active_weight
        report.enroll_product_BL_active_weight += enroll_product_BL_active_weight
        report.enroll_product_GM_inactive_weight += enroll_product_GM_inactive_weight
        report.enroll_product_GL_inactive_weight += enroll_product_GL_inactive_weight
        report.enroll_product_IL_inactive_weight += enroll_product_IL_inactive_weight
        report.enroll_product_ID_inactive_weight += enroll_product_ID_inactive_weight
        report.enroll_product_BM_inactive_weight += enroll_product_BM_inactive_weight
        report.enroll_product_BL_inactive_weight += enroll_product_BL_inactive_weight
        report.save()       

        current_month_start_date = (current_month_start_date+one_month).replace(day=1)
        current_month_end_date = (current_month_start_date + relativedelta(months=1)) - timedelta(days=1)
    Constants.ENROLL_PRODUCT_RUNNING_PAGE = Constants.ENROLL_PRODUCT_RUNNING_PAGE + 1
    if Constants.ENROLL_PRODUCT_RUNNING_PAGE> Constants.ENROLL_PRODUCT_MAX_PAGE_SIZE:
        Constants.ENROLL_PRODUCT_PROCESS_STATUS = ProcessStatus.SLEEP
        print("Enroll product statistics process ended for page  "+ str(Constants.ENROLL_PRODUCT_RUNNING_PAGE-1))
        print("Enroll product statistics process finished!. Will process after 24 hours again")
    else:
        Constants.ENROLL_PRODUCT_PROCESS_STATUS = ProcessStatus.AVAILABLE
        print("Enroll product statistics process ended for page  "+ str(Constants.ENROLL_PRODUCT_RUNNING_PAGE-1))
