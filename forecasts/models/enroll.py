from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Enroll(BaseModel):
    policy_number = models.CharField(max_length=20, unique=True)
    applicant_name = models.CharField(max_length=100)
    enrollment_date = models.DateField(default=timezone.now)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.policy_number} - {self.applicant_name}"
    