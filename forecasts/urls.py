from django.urls import path
from .views.predict_claim_views import PredictClaimAmountView

urlpatterns = [
    path('api/forecast/predict_claim_amount/', PredictClaimAmountView.as_view(), name='predict_claim_amount')
]
