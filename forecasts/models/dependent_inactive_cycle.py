from django.db import models
from forecasts.models.inactive_cycle import InactiveCycle

class DependentInactiveCycle(InactiveCycle):
    dependent_id = models.IntegerField()

    def __str__(self):
        return self.dependent_id + " - " + self.start_date + " - " + self.end_date