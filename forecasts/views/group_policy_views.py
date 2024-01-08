# insurance/views/group_policy_views.py
from rest_framework import generics
from forecasts.models.group_policy import GroupPolicy
from forecasts.serializers.group_policy_serializer import GroupPolicySerializer

class GroupPolicyList(generics.ListCreateAPIView):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer

class GroupPolicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupPolicy.objects.all()
    serializer_class = GroupPolicySerializer
