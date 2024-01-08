from django.utils import timezone
from django.db import models
from forecasts.models.base_model import BaseModel

class Enroll(BaseModel):
    group_policy_id = models.IntegerField()
    certificate_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, default='o')
    birth_date = models.DateField(default=timezone.now)
    effective_date = models.DateField(default=timezone.now)
    group_policy_cluster_id = models.IntegerField()

    def __str__(self):
        return f"{self.clics_db_id} - {self.certificate_number}"
    