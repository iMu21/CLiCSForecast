from datetime import timedelta
from django.db import models
from dateutil.relativedelta import relativedelta
from forecasts.models.base_model import BaseModel
from forecasts.models.group_policy_cluster_inactive_cycle import GroupPolicyClusterInactiveCycle

class GroupPolicyCluster(BaseModel):
    group_policy_id = models.IntegerField(null=True)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_id}'
