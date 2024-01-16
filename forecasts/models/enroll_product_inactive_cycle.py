from django.db import models
from forecasts.models.inactive_cycle import InactiveCycle

class EnrollProductInactiveCycle(InactiveCycle):
    enroll_product_id = models.IntegerField()

    def __str__(self):
        return self.enroll_product_id + " - " + self.start_date + " - " + self.end_date