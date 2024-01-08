# insurance/serializers/dependent_serializer.py
from rest_framework import serializers
from forecasts.models.dependent import Dependent

class DependentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependent
        fields = '__all__'
