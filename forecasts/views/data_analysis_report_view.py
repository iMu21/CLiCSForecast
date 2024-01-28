from rest_framework import generics
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast
from rest_framework import pagination
from forecasts.serializers.data_analysis_report_serializer import DataAnalysisReportClaimForecastSerializer

class DataAnalaysisReportClaimForecastModelPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100 

class DataAnalaysisReportClaimForecastList(generics.ListCreateAPIView):
    queryset = DataAnalaysisReportClaimForecast.objects.all()
    serializer_class = DataAnalysisReportClaimForecastSerializer
    pagination_class = DataAnalaysisReportClaimForecastModelPagination