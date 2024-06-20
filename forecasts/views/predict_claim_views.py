from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from forecasts.services.prediction_service import predict_monthly_payment_amount,predict_monthly_payment_amount_with_data
from django.http import JsonResponse

class PredictClaimAmountView(APIView):
    def get(self, request, format=None):
        predicted_claim = predict_monthly_payment_amount()
        return Response(predicted_claim, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            data = request.data
            if not data:
                return JsonResponse({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
            predicted_claim = predict_monthly_payment_amount_with_data(data)
            return Response(predicted_claim, status=status.HTTP_200_OK)
        except ValueError as ve:
            return JsonResponse({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
