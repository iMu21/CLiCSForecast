from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.group_policy_product_inactive_cycle import GroupPolicyProductInactiveCycle

class GroupPolicyProduct(BaseModel):
    group_policy_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_id}'
  