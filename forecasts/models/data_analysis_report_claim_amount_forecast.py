from django.db import models
import csv
import datetime
from forecasts.models.base_model import BaseModel
from forecasts.models.dependent_product import DependentProduct
from forecasts.models.group_policy import GroupPolicy
from forecasts.models.group_policy_cluster import GroupPolicyCluster
from forecasts.models.group_policy_cluster_product import GroupPolicyClusterProduct
from forecasts.models.group_policy_product import GroupPolicyProduct
from forecasts.models.payment_queue import PaymentQueue

class DataAnalaysisReportClaimForecast():
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    group_policy = models.IntegerField(default=0)
    group_policy_cluster = models.IntegerField(default=0)
    group_policy_product = models.IntegerField(default=0)
    group_policy_cluster_product = models.IntegerField(default=0)
    enroll = models.IntegerField(default=0)
    enroll_product = models.IntegerField(default=0)
    dependent = models.IntegerField(default=0)
    dependent_product = models.IntegerField(default=0)
    claim_amount = models.IntegerField(default=0)

    def __init__(self, year, month, group_policy, group_policy_cluster, group_policy_product,
                 group_policy_cluster_product, enroll, enroll_product, dependent, dependent_product,
                 claim_amount, *args, **kwargs):
        super(DataAnalaysisReportClaimForecast, self).__init__(*args, **kwargs)

        self.year = year
        self.month = month
        self.group_policy = group_policy
        self.group_policy_cluster = group_policy_cluster
        self.group_policy_product = group_policy_product
        self.group_policy_cluster_product = group_policy_cluster_product
        self.enroll = enroll
        self.enroll_product = enroll_product
        self.dependent = dependent
        self.dependent_product = dependent_product
        self.claim_amount = claim_amount

    @classmethod
    def get_reports(self):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2023, 12, 30)

        group_policy = self.CountIds(GroupPolicy.get_active_count_for_date_range(start_date, end_date))
        group_policy_cluster = self.CountIds(GroupPolicyCluster.get_active_count_for_date_range(start_date, end_date))
        group_policy_product = self.CountIds( GroupPolicyProduct.get_active_count_for_date_range(start_date, end_date))
        group_policy_cluster_product =self.CountIds(  GroupPolicyClusterProduct.get_active_count_for_date_range(start_date, end_date))
        #enroll = self.CountIds( Enroll.get_active_count_for_date_range(start_date, end_date))
        #enroll_product = self.CountIds( EnrollProduct.get_active_count_for_date_range(start_date, end_date))
        #dependent = self.CountIds( Dependent.get_active_count_for_date_range(start_date, end_date))
        dependent_product = self.CountIds( DependentProduct.get_active_count_for_date_range(start_date, end_date))
        payments = PaymentQueue.get_payment_amount_for_date_range(start_date, end_date)

        reports =[]

        for i in range(int(len(group_policy))):
            month = group_policy[i]['month']
            year = group_policy[i]['year']
            report = DataAnalaysisReportClaimForecast(
                year = year,
                month = month,
                group_policy = group_policy[i]['count'],
                group_policy_cluster = group_policy_cluster[i]['count'],
                group_policy_product = group_policy_product[i]['count'],
                group_policy_cluster_product = group_policy_cluster_product[i]['count'],
                enroll = 0,
                enroll_product = 0,
                dependent =0 ,
                dependent_product = dependent_product[i]['count'],
                claim_amount = payments[i]['amount']
            )

            reports.append(report)
        
        return reports

    @classmethod
    def CountIds(self,result):
        for res in result:
            res['count'] = len(res['ids'])
            res['ids'] = None
        return result
    
    @classmethod
    def generate_report(self):
        objects_list = self.get_reports()
        csv_file_path = BaseModel.get_file_path('data_analysis_reports','DataAnalaysisReportClaimForecast.csv')
        with open(csv_file_path,  'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            model_fields = ['year','month','group_policy',
                            'group_policy_cluster','group_policy_product',
                            'group_policy_cluster_product','enroll',
                            'enroll_product','dependent',
                            'dependent_product','claim_amount']
            
            csv_writer.writerow(model_fields)

            for obj in objects_list:
                    csv_writer.writerow([getattr(obj, field) for field in model_fields])