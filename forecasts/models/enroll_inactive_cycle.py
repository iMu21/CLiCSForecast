from django.db import models
from forecasts.models.base_model import BaseModel

class EnrollInactiveCycle(BaseModel):
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.enroll_id 