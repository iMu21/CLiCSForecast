from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Product(BaseModel):
    clics_db_id = models.IntegerField()
    code = models.CharField(max_length=20)
    claim_type = models.CharField()
    waiting_period = models.IntegerField()
    max_limit = models.FloatField()
    maximum_age = models.IntegerField()
    product_category = models.CharField()
    lob = models.CharField()


    def __str__(self):
        return f'{self.code}'
    