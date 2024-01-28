from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class GroupPolicy(BaseModel):
    group_number = models.CharField(max_length=100)
    premium_payment_type = models.CharField(max_length=100)
    group_policy_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.group_number}'