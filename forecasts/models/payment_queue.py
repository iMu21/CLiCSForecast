from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.claim_entry import ClaimEntry

class PaymentQueue(BaseModel):
    claim_entry_id = models.IntegerField(default=0)
    claim_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    payable_amount = models.DecimalField(max_digits = 30, decimal_places = 3)

    def __str__(self):
        return self.claim_entry_id
