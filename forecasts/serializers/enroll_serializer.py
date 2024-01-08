# insurance/serializers/enroll_serializer.py
from rest_framework import serializers
from forecasts.models.enroll import Enroll

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = '__all__'
