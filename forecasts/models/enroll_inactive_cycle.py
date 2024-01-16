from django.db import models
from forecasts.models.inactive_cycle import InactiveCycle

class EnrollInactiveCycle(InactiveCycle):
    enroll_id = models.IntegerField()

    def __str__(self):
        return self.enroll_id + " - " + self.start_date + " - " + self.end_date