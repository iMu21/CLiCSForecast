from django.db import models
from django.utils import timezone
from forecasts.models.base_model import BaseModel

class InactiveCycle(BaseModel):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.start_date + " - " + self.end_date