from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    predicted_claim = serializers.DecimalField(max_digits=30, decimal_places=2)
