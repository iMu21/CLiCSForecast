from django.db import models
from forecasts.models.base_model import BaseModel

class Dependent(BaseModel):
    #enroll = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.dependent_name} "#- {self.enroll}"
