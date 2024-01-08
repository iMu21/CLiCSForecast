from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..scikit_learn_forecastings import predict_next_month_claim_amount
from forecasts.serializers.predict_claim_amount_serializer import PredictionSerializer

class PredictClaimAmountView(APIView):
    def get(self, request, format=None):
        predicted_claim = predict_next_month_claim_amount()

        # Serialize the prediction
        serializer = PredictionSerializer({'predicted_claim': predicted_claim})

        return Response(serializer.data, status=status.HTTP_200_OK)
