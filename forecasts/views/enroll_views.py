from rest_framework import generics
from forecasts.models.enroll import Enroll
from forecasts.serializers.enroll_serializer import EnrollSerializer

class EnrollList(generics.ListCreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer
