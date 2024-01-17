from rest_framework.views import APIView
from forecasts.models import *
from rest_framework.response import Response
from rest_framework import status

class EnrollBulkUpload(APIView):
    def get(self, request, format=None):
        Enroll.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class EnrollInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        EnrollInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class EnrollProductBulkUpload(APIView):
    def get(self, request, format=None):
        EnrollProduct.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class EnrollProductInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        EnrollProductInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class DependentBulkUpload(APIView):
    def get(self, request, format=None):
        Dependent.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class DependentInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        DependentInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class DependentProductBulkUpload(APIView):
    def get(self, request, format=None):
        DependentProduct.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class DependentProductInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        DependentProductInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicy.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class GroupPolicyproductBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyProduct.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyproductInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyProductInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyClusterBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyCluster.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyClusterProductBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyClusterProduct.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyClusterProductInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyClusterProductInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)

class GroupPolicyClusterInactiveCycleBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicyClusterInactiveCycle.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class PaymentQueueBulkUpload(APIView):
    def get(self, request, format=None):
        PaymentQueue.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class ProductBulkUpload(APIView):
    def get(self, request, format=None):
        Product.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class ClaimEntryBulkUpload(APIView):
    def get(self, request, format=None):
        ClaimEntry.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class AllBulkUpload(APIView):
    def get(self, request, format=None):
        Enroll.bulk_upload()
        EnrollInactiveCycle.bulk_upload()
        EnrollProduct.bulk_upload()
        EnrollProductInactiveCycle.bulk_upload()
        Dependent.bulk_upload()
        DependentInactiveCycle.bulk_upload()
        DependentProduct.bulk_upload()
        DependentProductInactiveCycle.bulk_upload()
        GroupPolicy.bulk_upload()
        GroupPolicyProduct.bulk_upload()
        GroupPolicyProductInactiveCycle.bulk_upload()
        GroupPolicyInactiveCycle.bulk_upload()
        GroupPolicyCluster.bulk_upload()
        GroupPolicyClusterProduct.bulk_upload()
        GroupPolicyClusterProductInactiveCycle.bulk_upload()
        GroupPolicyClusterInactiveCycle.bulk_upload()
        PaymentQueue.bulk_upload()
        Product.bulk_upload()
        ClaimEntry.bulk_upload()