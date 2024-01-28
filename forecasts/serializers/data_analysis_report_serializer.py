from rest_framework import serializers
from forecasts.models.data_analysis_report_claim_amount_forecast import DataAnalaysisReportClaimForecast

class DataAnalysisReportClaimForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnalaysisReportClaimForecast
        fields = '__all__'