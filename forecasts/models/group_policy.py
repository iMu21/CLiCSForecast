from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class GroupPolicy(BaseModel):
    group_name = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.group_name
