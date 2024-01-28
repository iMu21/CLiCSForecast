from django.urls import path
from forecasts.views.claim_amount_forecast_training_data_view import *
from forecasts.views.data_analysis_report_view import DataAnalaysisReportClaimForecastList
from .views.enroll_views import EnrollList,EnrollDetail
from .views.predict_claim_views import PredictClaimAmountView
from .views.bulk_upload_view import *

urlpatterns = [
    path('api/enroll/get-page/', EnrollList.as_view(), name='enrolls'),
    path('api/enroll/<int:pk>/', EnrollDetail.as_view(), name='enroll'),

    path('api/forecast/predict_claim_amount/', PredictClaimAmountView.as_view(), name='predict_claim_amount'),
    
    path('api/generate-report/claim-amount-forecast/', DataAnalaysisReportClaimForecastView.as_view()),

    path('api/get-data-analysis-reports/claim-amount-forecast',DataAnalaysisReportClaimForecastList.as_view()),

    path('api/bulk-upload/all/', AllBulkUpload.as_view(), name='All Bulk Upload'),
    path('api/bulk-upload/group-policy/', GroupPolicyBulkUpload.as_view()),
    path('api/bulk-upload/enroll/', EnrollBulkUpload.as_view()),
    path('api/bulk-upload/enroll-inactive-cycle/', EnrollInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/enroll-product/', EnrollProductBulkUpload.as_view()),
    path('api/bulk-upload/enroll-product-inactive-cycle/', EnrollProductInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/dependent/', DependentBulkUpload.as_view()),
    path('api/bulk-upload/dependent-inactive-cycle/', DependentInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/dependent-product/', DependentProductBulkUpload.as_view()),
    path('api/bulk-upload/dependent-product-inactive-cycle/', DependentProductInactiveCycleBulkUpload.as_view()),
    
    path('api/bulk-upload/product/', ProductBulkUpload.as_view()),
    
    path('api/bulk-upload/group-policy/', GroupPolicyBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-cluster/', GroupPolicyClusterBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-product/', GroupPolicyproductBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-inactive-cycle/', GroupPolicyInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-cluster-product/', GroupPolicyClusterProductBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-cluster-inactive-cycle/', GroupPolicyClusterInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-product-inactive-cycle/', GroupPolicyproductInactiveCycleBulkUpload.as_view()),
    path('api/bulk-upload/group-policy-cluster-product-inactive-cycle/', GroupPolicyClusterProductInactiveCycleBulkUpload.as_view()),

    path('api/bulk-upload/claim-entry/', ClaimEntryBulkUpload.as_view()),
    path('api/bulk-upload/payment-queue/', PaymentQueueBulkUpload.as_view()),
]
