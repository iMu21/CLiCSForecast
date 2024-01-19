import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from forecasts.models.dependent_product import DependentProduct
from forecasts.models.group_policy import GroupPolicy
from forecasts.models.group_policy_cluster import GroupPolicyCluster
from forecasts.models.group_policy_cluster_product import GroupPolicyClusterProduct
from forecasts.models.group_policy_product import GroupPolicyProduct
from forecasts.models.payment_queue import PaymentQueue

class ActiveCountView(APIView):
    def get(self, request, format=None):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2023, 12, 30)

        result =[]

        group_policy = self.CountIds(GroupPolicy.get_active_count_for_date_range(start_date, end_date))
        group_policy_cluster = self.CountIds(GroupPolicyCluster.get_active_count_for_date_range(start_date, end_date))
        group_policy_product = self.CountIds( GroupPolicyProduct.get_active_count_for_date_range(start_date, end_date))
        group_policy_cluster_product =self.CountIds(  GroupPolicyClusterProduct.get_active_count_for_date_range(start_date, end_date))
        #enroll = self.CountIds( Enroll.get_active_count_for_date_range(start_date, end_date))
        #enroll_product = self.CountIds( EnrollProduct.get_active_count_for_date_range(start_date, end_date))
        #dependent = self.CountIds( Dependent.get_active_count_for_date_range(start_date, end_date))
        dependent_product = self.CountIds( DependentProduct.get_active_count_for_date_range(start_date, end_date))
        payments = PaymentQueue.get_payment_amount_for_date_range(start_date, end_date)

        for i in range(int(len(group_policy))):
            month = group_policy[i]['month']
            year = group_policy[i]['year']
           
            result.append({
                'year': year,
                'month' : month,
                'group_policy' : group_policy[i]['count'],
                'group_policy_cluster': group_policy_cluster[i]['count'],
                'group_policy_product': group_policy_product[i]['count'],
                'group_policy_cluster_product': group_policy_cluster_product[i]['count'],
                #'enroll': enroll[i]['count'],
                #'enroll_product': enroll_product[i]['count'],
                #'dependent': dependent[i]['count'],
                 'dependent_product': dependent_product[i]['count'],
                 'total_claims' : payments[i]['amount']
            })

        return Response(result, status=status.HTTP_200_OK)
    
    @classmethod
    def CountIds(self,result):
        for res in result:
            res['count'] = len(res['ids'])
            res['ids'] = None
        return result
    
class ActiveGroupPolicyCountView(APIView):
    def get(self, request, format=None):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2023, 12, 30)

        result = GroupPolicy.get_active_count_for_date_range(start_date, end_date)
        for res in result:
            res['count'] = len(res['ids'])
            res['ids'] = None

        return Response(result, status=status.HTTP_200_OK)
    
class ActiveGroupPolicyProductCountView(APIView):
    def get(self, request, format=None):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2023, 12, 30)

        result = GroupPolicyProduct.get_active_count_for_date_range(start_date, end_date)
        for res in result:
            res['count'] = len(res['ids'])
            res['ids'] = None

        return Response(result, status=status.HTTP_200_OK)
    
class ActiveGroupPolicyClusterCountView(APIView):
    def get(self, request, format=None):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2023, 12, 30)

        result = GroupPolicyCluster.get_active_count_for_date_range(start_date, end_date)
        for res in result:
            res['count'] = len(res['ids'])
            res['ids'] = None

        return Response(result, status=status.HTTP_200_OK)
    
class DataAnalaysisReportClaimForecastView(APIView):
    def get(self, request, format=None):
        DataAnalaysisReportClaimForecast.generate_report()
        return Response({'status':'done'}, status=status.HTTP_200_OK)
    