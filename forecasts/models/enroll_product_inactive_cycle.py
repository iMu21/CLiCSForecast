from django.db import models
from forecasts.models.base_model import BaseModel

class EnrollProductInactiveCycle(BaseModel):
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.parent_id + " - " + self.start_date + " - " + self.end_date