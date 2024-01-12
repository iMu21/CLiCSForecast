from rest_framework import generics
from forecasts.models.dependent import Dependent
from forecasts.serializers.dependent_serializer import DependentSerializer
from rest_framework import pagination

class DependentPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 500 

class DependentList(generics.ListCreateAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer
    pagination_class = DependentPagination

class DependentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer
