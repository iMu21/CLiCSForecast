from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class GroupPolicyCluster(BaseModel):
    group_policy_id = models.IntegerField(null=True)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_id}'
    