from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Product(BaseModel):
    clics_db_id = models.IntegerField()
    code = models.CharField(max_length=50)
    claim_type = models.CharField(max_length=50)
    maximum_age = models.IntegerField(null=True)
    product_category = models.CharField(max_length=50)
    lob = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.code}'
    