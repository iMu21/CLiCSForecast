from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from forecasts.services.prediction_service import predict_monthly_payment_amount

class PredictClaimAmountView(APIView):
    def get(self, request, format=None):
        predicted_claim = predict_monthly_payment_amount()

        return Response(predicted_claim, status=status.HTTP_200_OK,)
