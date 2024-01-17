from django.urls import path
from .views.enroll_views import EnrollList,EnrollDetail
from .views.dependent_views import DependentList
from .views.group_policy_views import GroupPolicyList
from .views.predict_claim_views import PredictClaimAmountView
from .views.bulk_upload_view import *

urlpatterns = [
    path('api/enrolls/', EnrollList.as_view(), name='enrolls'),
    path('api/enroll/<int:pk>/', EnrollDetail.as_view(), name='enroll'),

    path('api/group-policy-bulk-upload/', GroupPolicyBulkUpload.as_view(), name='group-policy-bulk-upload'),
    path('api/enroll-bulk-upload/', EnrollBulkUpload.as_view(), name='enroll-bulk-upload'),
    path('api/dependent-bulk-upload/', DependentBulkUpload.as_view(), name='dependent-bulk-upload'),

    path('api/dependent/', DependentList.as_view(), name='dependent-list'),
    path('api/group_policy/', GroupPolicyList.as_view(), name='group-policy-list'),
    path('api/predict_claim_amount/', PredictClaimAmountView.as_view(), name='predict_claim_amount'),

    path('api/all-bulk-upload/', AllBulkUpload.as_view(), name='All Bulk Upload'),
]
