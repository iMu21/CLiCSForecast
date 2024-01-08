# forecasts/models/base_model.py
from django.db import models
import csv
import os

class BaseModel(models.Model):
    clics_db_id = models.IntegerField(unique = True)

    class Meta:
        abstract = True  # This model will not be created as a database table

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)

        # Determine the CSV file path dynamically based on the model's name
        model_name = self.__class__.__name__.lower()
        app_folder = os.path.dirname(os.path.abspath(__file__))
        project_folder = os.path.dirname(app_folder)
        csv_folder = os.path.join(project_folder, 'csv_data')
        os.makedirs(csv_folder, exist_ok=True)
        csv_file_path = os.path.join(csv_folder, f'{model_name}_data.csv')

        is_new_file = not os.path.isfile(csv_file_path)

        fields = [field.name for field in self._meta.fields]

        with open(csv_file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if is_new_file:
                # Write header if it's a new file
                csv_writer.writerow(fields)

            csv_writer.writerow([getattr(self, field) for field in fields])

        # Optionally, you may want to create a backup after each update
        self.create_backup(csv_folder, model_name)

    def create_backup(self, csv_folder, model_name):
        # Add your backup logic here
        pass
