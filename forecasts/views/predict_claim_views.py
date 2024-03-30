from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from forecasts.services.prediction_service import predict_monthly_payment_amount
from ..scikit_learn_forecastings import predict_next_month_claim_amount
from forecasts.serializers.predict_claim_amount_serializer import PredictionSerializer

class PredictClaimAmountView(APIView):
    def get(self, request, format=None):
        predicted_claim = predict_monthly_payment_amount()

        # Serialize the prediction
        #serializer = PredictionSerializer({'predicted_claim': predicted_claim})

        return Response(predicted_claim, status=status.HTTP_200_OK)
