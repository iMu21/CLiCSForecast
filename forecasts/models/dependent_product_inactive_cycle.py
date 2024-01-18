from django.db import models
from forecasts.models.base_model import BaseModel

class DependentProductInactiveCycle(BaseModel):
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    dependent_product_id = models.IntegerField(default=0)

    def __str__(self):
        return self.dependent_product_id