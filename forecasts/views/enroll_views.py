from rest_framework.views import APIView
from rest_framework import generics
from forecasts.models.enroll import Enroll
from rest_framework.response import Response
from rest_framework import status
from forecasts.serializers.enroll_serializer import EnrollSerializer

class EnrollList(generics.ListCreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer