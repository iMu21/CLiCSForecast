from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.dependent_product_inactive_cycle import DependentProductInactiveCycle
from datetime import timedelta
from dateutil.relativedelta import relativedelta
class DependentProduct(BaseModel):
    dependent_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    group_policy_cluster_product_id = models.IntegerField(default=0)
    coverage_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    effective_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.clics_db_id}"
    