# insurance/views/group_policy_views.py
from rest_framework import generics
from forecasts.models.group_policy import GroupPolicy
from rest_framework import pagination
from forecasts.serializers.group_policy_serializer import GroupPolicySerializer

class GroupPolicyModelPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100 

class GroupPolicyList(generics.ListCreateAPIView):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
    pagination_class = GroupPolicyModelPagination

class GroupPolicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
