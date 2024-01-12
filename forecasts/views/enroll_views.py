from rest_framework.views import APIView
from rest_framework import generics
from forecasts.models.enroll import Enroll
from rest_framework.response import Response
from rest_framework import pagination
from forecasts.serializers.enroll_serializer import EnrollSerializer

class EnrollModelPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100 

class EnrollList(generics.ListCreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer
    pagination_class = EnrollModelPagination

class EnrollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer