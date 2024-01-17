from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class GroupPolicyProduct(BaseModel):
    group_policy_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_id}'
    