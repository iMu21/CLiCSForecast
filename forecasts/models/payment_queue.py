from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel
from datetime import timedelta
from django.db import models
from dateutil.relativedelta import relativedelta

class PaymentQueue(BaseModel):
    claim_entry_id = models.IntegerField(default=0)
    claim_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    payable_amount = models.DecimalField(max_digits = 30, decimal_places = 3)
    claim_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.claim_entry_id
        
    @classmethod
    def get_payment_amount_for_date_range(self,start_date, end_date):
        payment_dict = []

        current_start_date = start_date.replace(day=1)
        current_end_date = (start_date + relativedelta(months=1)) - timedelta(days=1)

        one_month = timedelta(days=31)
        payments = PaymentQueue.objects.all()

        while current_end_date <= end_date:
            amount = 0
            for payment in payments:
                if current_start_date<=payment.claim_date<=current_end_date:
                    amount = amount + payment.claim_amount
            payment_dict.append({
                'year': current_start_date.year,
                'month': current_start_date.month,
                'amount': amount
            })

            current_start_date = (current_start_date+one_month).replace(day=1)
            current_end_date = (current_start_date + relativedelta(months=1)) - timedelta(days=1)

        return payment_dict
