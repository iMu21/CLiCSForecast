from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Dependent(BaseModel):
    #enroll = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=100, default=timezone.now)
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.dependent_name} "#- {self.enroll}"
