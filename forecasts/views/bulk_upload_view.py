from rest_framework.views import APIView
from forecasts.models import Enroll,Dependent,GroupPolicy
from rest_framework.response import Response
from rest_framework import status

class EnrollBulkUpload(APIView):
    def get(self, request, format=None):
        Enroll.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class DependentBulkUpload(APIView):
    def get(self, request, format=None):
        Dependent.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)
    
class GroupPolicyBulkUpload(APIView):
    def get(self, request, format=None):
        GroupPolicy.bulk_upload()
        return Response({'Status': "Done"}, status=status.HTTP_200_OK)