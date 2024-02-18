from datetime import timedelta
from dateutil.relativedelta import relativedelta
from forecasts.constants import Constants, ProcessStatus
from forecasts.models.dependent import Dependent
from forecasts.models.dependent_inactive_cycle import DependentInactiveCycle
from forecasts.models.dependent_product import DependentProduct
from forecasts.models.dependent_product_inactive_cycle import DependentProductInactiveCycle
from forecasts.models.enroll import Enroll
from forecasts.models.enroll_inactive_cycle import EnrollInactiveCycle
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.group_policy_cluster_inactive_cycle import GroupPolicyClusterInactiveCycle
from forecasts.models.group_policy_inactive_cycle import GroupPolicyInactiveCycle
from forecasts.models.product import Product
from forecasts.services.inactive_cycle_service import is_inactive_on_date

def update_dependent_product_statistics():
    if Constants.DEPENDENT_PRODUCT_PROCESS_STATUS == ProcessStatus.AVAILABLE:
        Constants.DEPENDENT_PRODUCT_PROCESS_STATUS = ProcessStatus.PROCESSING
        print("Dependent product statistics process start for page  "+ str(Constants.DEPENDENT_PRODUCT_RUNNING_PAGE))
    else:
        print("Already processing")
        return
    
    to_id = Constants.DEPENDENT_PRODUCT_BATCH_SIZE * Constants.DEPENDENT_PRODUCT_RUNNING_PAGE
    from_id = (Constants.DEPENDENT_PRODUCT_BATCH_SIZE * (Constants.DEPENDENT_PRODUCT_RUNNING_PAGE+1))-1
    current_month_start_date = Constants.REPORT_START_DATE.replace(day=1)
    current_month_end_date = (Constants.REPORT_START_DATE + relativedelta(months=1)) - timedelta(days=1)

    one_month = timedelta(days=31)
    one_day = timedelta(days=1)

    dependent_products = DependentProduct.objects.filter(clics_db_id__lt=from_id,clics_db_id__gt = to_id)
    sorted_inactive_cycles = DependentProductInactiveCycle.objects.filter(parent_id__lt=from_id,parent_id__gt = to_id).order_by('parent_id','start_date','end_date')
    
    sorted_dependent_inactive_cycles = DependentInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_enroll_inactive_cycles = EnrollInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_inactive_cycles = GroupPolicyInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_cluster_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    sorted_group_policy_cluster_product_inactive_cycles = GroupPolicyClusterInactiveCycle.objects.all().order_by('parent_id','start_date','end_date')
    
    dp_enroll_inactive_cycle_map = {}
    dp_dependent_inactive_cycle_map = {}
    dp_group_policy_inactive_cycle_map = {}
    dp_group_policy_cluster_inactive_cycle_map = {}
    dp_group_policy_cluster_product_inactive_cycle_map = {}

    while current_month_end_date <= Constants.REPORT_END_DATE:
        print("Dependent product checking for "+ str(current_month_end_date.year)+"-"+ str(current_month_end_date.month))
        total_inactive_weight = int(0)
        total_active_weight = int(0)
        total_active_at_least_one_day = int(0)
        dependent_product_GM_active_weight = int(0)
        dependent_product_GL_active_weight = int(0)
        dependent_product_BM_active_weight = int(0)
        dependent_product_BL_active_weight = int(0)
        dependent_product_GM_inactive_weight = int(0)
        dependent_product_GL_inactive_weight = int(0)
        dependent_product_BM_inactive_weight = int(0)
        dependent_product_BL_inactive_weight = int(0)

        for dependent_product in dependent_products:
            product = Product.objects.get(clics_db_id= dependent_product.product_id)
            dependent = Dependent.objects.get(clics_db_id= dependent_product.dependent_id)
            enroll = Enroll.objects.get(clics_db_id= dependent.enroll_id)
            date = current_month_start_date
            is_active_in_month = False
            while date <= current_month_end_date:
                if dependent_product.effective_date <= date:
                    is_enroll_inactive = False
                    is_dependent_inactive = False
                    is_group_policy_inactive = False
                    is_group_policy_cluster_inactive = False
                    is_group_policy_cluster_product_inactive = False

                    #group policy
                    key = str(enroll.group_policy_id)+"-"+str(date.day)+"-"+str(date.month)+"-"+str(date.year)
                    if key in dp_group_policy_inactive_cycle_map:
                        is_group_policy_inactive = dp_group_policy_inactive_cycle_map[key]
                    else:
                        is_group_policy_inactive = is_inactive_on_date(sorted_group_policy_inactive_cycles,enroll.group_policy_id,date)
                        dp_group_policy_inactive_cycle_map[key] = is_group_policy_inactive
                    
                    #print("Group policy checked "+ str(enroll.group_policy_id))

                    if not is_group_policy_inactive:
                        #group policy cluster
                        key = str(enroll.group_policy_cluster_id)+"-"+str(date.day)+"-"+str(date.month)+"-"+ str(date.year)
                        if key in dp_group_policy_cluster_inactive_cycle_map:
                            is_group_policy_cluster_inactive = dp_group_policy_cluster_inactive_cycle_map[key]
                        else:
                            is_group_policy_cluster_inactive = is_group_policy_inactive or (
                                is_inactive_on_date(sorted_group_policy_cluster_inactive_cycles,enroll.group_policy_cluster_id,date))
                            dp_group_policy_cluster_inactive_cycle_map[key] = is_group_policy_cluster_inactive
                        
                        #print("Group policy clucster checked "+ str(enroll.group_policy_cluster_id))

                        if not is_group_policy_cluster_inactive:
                            #group policy cluster product
                            key = str(dependent_product.group_policy_cluster_product_id)+"-"+str(date.day)+"-"+str(date.month)+"-"+str(date.year)
                            if key in dp_group_policy_cluster_product_inactive_cycle_map:
                                is_group_policy_cluster_product_inactive = dp_group_policy_cluster_product_inactive_cycle_map[key]
                            else:
                                is_group_policy_cluster_product_inactive = is_group_policy_cluster_inactive or(
                                is_inactive_on_date(sorted_group_policy_cluster_product_inactive_cycles,dependent_product.group_policy_cluster_product_id,date))
                                dp_group_policy_cluster_product_inactive_cycle_map[key] = is_group_policy_cluster_product_inactive
                            #print("Group policy clucster product checked "+ str(dependent_product.group_policy_cluster_product_id))

                            #enroll
                            key = str(enroll.clics_db_id)+"-"+str(date.day)+"-"+str(date.month)+"-"+str(date.year)
                            if key in dp_enroll_inactive_cycle_map:
                                is_enroll_inactive = dp_enroll_inactive_cycle_map[key]
                            else:
                                is_enroll_inactive = is_group_policy_cluster_inactive or ( 
                                    is_inactive_on_date(sorted_enroll_inactive_cycles,enroll.clics_db_id,date))
                                dp_enroll_inactive_cycle_map[key] = is_enroll_inactive
                            #print("Enroll checked "+ str(enroll.clics_db_id))

                            if not is_enroll_inactive:
                                #dependent
                                key = str(dependent.clics_db_id)+"-"+str(date.day)+"-"+str(date.month)+"-"+str(date.year)
                                if key in dp_dependent_inactive_cycle_map:
                                    is_dependent_inactive = dp_dependent_inactive_cycle_map[key]
                                else:
                                    is_dependent_inactive = is_enroll_inactive or (
                                        is_inactive_on_date(sorted_dependent_inactive_cycles,dependent.clics_db_id,date))
                                    dp_dependent_inactive_cycle_map[key] = is_dependent_inactive
                                #print("Enroll checked "+ str(dependent.clics_db_id))

                    
                    if (is_group_policy_inactive)or ( 
                        is_group_policy_cluster_inactive)or ( 
                        is_enroll_inactive)or ( 
                        is_dependent_inactive) or ( 
                        is_group_policy_cluster_product_inactive)or ( 
                        is_inactive_on_date(sorted_inactive_cycles,dependent_product.clics_db_id,date)):
                        total_inactive_weight+=1
                        if product.claim_type == "GM":
                            dependent_product_GM_inactive_weight+=1
                        elif product.claim_type == "GL":
                            dependent_product_GL_inactive_weight+=1
                        elif product.claim_type == "BM":
                            dependent_product_BM_inactive_weight+=1
                        elif product.claim_type == "BL":
                            dependent_product_BL_inactive_weight+=1
                    else:
                        total_active_weight+=1
                        if product.claim_type == "GM":
                            dependent_product_GM_active_weight+=1
                        elif product.claim_type == "GL":
                            dependent_product_GL_active_weight+=1
                        elif product.claim_type == "BM":
                            dependent_product_BM_active_weight+=1
                        elif product.claim_type == "BL":
                            dependent_product_BL_active_weight+=1
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
                report.dependent_product_active_weight = 0
                report.dependent_product_inactive_weight = 0
                report.dependent_product_active_at_least_one_day = 0
                report.dependent_product_GM_active_weight = 0
                report.dependent_product_GL_active_weight = 0
                report.dependent_product_BM_active_weight = 0
                report.dependent_product_BL_active_weight = 0
                report.dependent_product_GM_inactive_weight = 0
                report.dependent_product_GL_inactive_weight = 0
                report.dependent_product_BM_inactive_weight = 0
                report.dependent_product_BL_inactive_weight = 0
        else:
            report = DataAnalaysisReportClaimForecast()
            report.year=year
            report.month = month

        report.dependent_product_active_weight += total_active_weight
        report.dependent_product_inactive_weight += total_inactive_weight
        report.dependent_product_active_at_least_one_day += total_active_at_least_one_day
        report.dependent_product_GM_active_weight += dependent_product_GM_active_weight
        report.dependent_product_GL_active_weight += dependent_product_GL_active_weight
        report.dependent_product_BM_active_weight += dependent_product_BM_active_weight
        report.dependent_product_BL_active_weight += dependent_product_BL_active_weight
        report.dependent_product_GM_inactive_weight += dependent_product_GM_inactive_weight
        report.dependent_product_GL_inactive_weight += dependent_product_GL_inactive_weight
        report.dependent_product_BM_inactive_weight += dependent_product_BM_inactive_weight
        report.dependent_product_BL_inactive_weight += dependent_product_BL_inactive_weight
        report.save()       

        current_month_start_date = (current_month_start_date+one_month).replace(day=1)
        current_month_end_date = (current_month_start_date + relativedelta(months=1)) - timedelta(days=1)
    Constants.DEPENDENT_PRODUCT_RUNNING_PAGE = Constants.DEPENDENT_PRODUCT_RUNNING_PAGE + 1
    if Constants.DEPENDENT_PRODUCT_RUNNING_PAGE> Constants.DEPENDENT_PRODUCT_MAX_PAGE_SIZE:
        Constants.DEPENDENT_PRODUCT_PROCESS_STATUS = ProcessStatus.SLEEP
        print("Dependent product statistics process ended for page  "+ str(Constants.DEPENDENT_PRODUCT_RUNNING_PAGE-1))
        print("Dependent product statistics process finished!. Will process after 24 hours again")
    else:
        Constants.DEPENDENT_PRODUCT_PROCESS_STATUS = ProcessStatus.AVAILABLE
        print("Dependent product statistics process ended for page  "+ str(Constants.DEPENDENT_PRODUCT_RUNNING_PAGE-1))
