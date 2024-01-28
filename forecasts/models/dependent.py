from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.dependent_inactive_cycle import DependentInactiveCycle
from datetime import timedelta
from dateutil.relativedelta import relativedelta
class Dependent(BaseModel):
    enroll_id = models.IntegerField(default=0)
    gender = models.CharField(max_length=1,default='O')
    birth_date = models.DateField(null=True,blank=True)
    effective_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.clics_db_id} - {self.enroll_id}"
