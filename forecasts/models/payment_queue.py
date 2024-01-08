from django.db import models
from forecasts.models.base_model import BaseModel
from forecasts.models.claim_entry import ClaimEntry

class PaymentQueue(BaseModel):
    claim_entry_db_id = models.IntegerField()
    #claim_entry = ClaimEntry.objects.get(db_id = claim_entry_db_id)
    claim_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    payable_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    effective_date = models.DateField()
    policy_number = models.CharField(max_length = 100)
    coverage_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    claim_number = models.CharField(max_length = 100)

    def __str__(self):
        return self.policy_number
