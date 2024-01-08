from django.db import models
from forecasts.models.base_model import BaseModel

class ClaimEntry(BaseModel):
    policy_number = models.CharField(max_length=100)
    claim_amount = models.DecimalField(max_digits=30, decimal_places=2)
    claim_date = models.DateField()

    def __str__(self):
        return self.policy_number
    