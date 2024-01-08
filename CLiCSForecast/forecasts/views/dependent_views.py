from rest_framework import generics
from CLiCSForecast.forecasts.models.dependent_models import Dependent
from forecasts.serializers.dependent_serializer import DependentSerializer

class DependentList(generics.ListCreateAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer

class DependentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer
