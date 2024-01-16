from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class GroupPolicyProduct(BaseModel):
    group_policy_id = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.group_policy_id}'
    