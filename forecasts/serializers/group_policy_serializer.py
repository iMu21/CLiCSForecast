from rest_framework import serializers
from forecasts.models.group_policy import GroupPolicy

class GroupPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPolicy
        fields = '__all__'
