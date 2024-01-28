from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.group_policy_cluster_product_inactive_cycle import GroupPolicyClusterProductInactiveCycle
from datetime import timedelta
from django.db import models

from dateutil.relativedelta import relativedelta
class GroupPolicyClusterProduct(BaseModel):
    group_policy_cluster_id = models.IntegerField(default=0)
    group_policy_product_id = models.IntegerField(default=0)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.group_policy_cluster_id}'
