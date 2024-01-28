from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from forecasts.services.data_analysis_report_claim_forecast_service import generate_report

class DataAnalaysisReportClaimForecastView(APIView):
    def get(self, request, format=None):
        generate_report()
        return Response({'status':'done'}, status=status.HTTP_200_OK)
    