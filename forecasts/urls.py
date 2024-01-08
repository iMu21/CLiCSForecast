from django.urls import path
from .views.enroll_views import EnrollList
from .views.dependent_views import DependentList
from .views.group_policy_views import GroupPolicyList
from .views.predict_claim_views import PredictClaimAmountView

urlpatterns = [
    path('api/enroll/', EnrollList.as_view(), name='enroll-list'),
    path('api/dependent/', DependentList.as_view(), name='dependent-list'),
    path('api/group_policy/', GroupPolicyList.as_view(), name='group-policy-list'),
    path('api/predict_claim_amount/', PredictClaimAmountView.as_view(), name='predict_claim_amount'),
]
