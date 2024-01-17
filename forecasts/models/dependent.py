from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Dependent(BaseModel):
    enroll_id = models.IntegerField(default=0)
    gender = models.CharField(max_length=1,default='O')
    birth_date = models.DateField(null=True)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.clics_db_id} - {self.enroll_id}"
