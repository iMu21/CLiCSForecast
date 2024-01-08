from django.utils import timezone
import shutil
from django.db import models
import csv
import os

class BaseModel(models.Model):
    clics_db_id = models.IntegerField(unique = True)

    class Meta:
        abstract = True  

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        csv_latest_path = self.__class__.get_csv_latest_file_path()
        
        is_new_file = not os.path.isfile(csv_latest_path)

        fields = [field.name for field in self._meta.fields]

        with open(csv_latest_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if is_new_file:
                csv_writer.writerow(fields)

            csv_writer.writerow([getattr(self, field) for field in fields])

    @classmethod
    def bulk_upload(self):
        self.back_up_existing()
        self.delete_existing()
        self.upload_data()
        self.export_model_to_csv()

    @classmethod
    def upload_data(self):
        csv_upload_path = self.get_csv_upload_file_path()
        with open(csv_upload_path, 'r') as csv_file: 
            reader = csv.DictReader(csv_file)
            for row in reader:
                obj = self(**row)
                obj.save()

    @classmethod
    def export_model_to_csv(self):
        csv_latest_path = self.get_csv_latest_file_path()
        os.path.isfile(csv_latest_path)
        field_names = [field.name for field in self._meta.get_fields()]

        with open(csv_latest_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(field_names)
            for obj in self.objects.all():
                row_values = [getattr(obj, field) for field in field_names]
                csv_writer.writerow(row_values)
    
    @classmethod
    def get_project_folder(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        project_folder = os.path.dirname(app_folder)
        return project_folder
    
    @classmethod
    def get_file_path(self,folder,file_name):
        project_folder = self.get_project_folder()
        folder = os.path.join(project_folder, folder)
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, file_name)
        return file_path 

    @classmethod
    def get_csv_latest_file_path(self):
        return self.get_file_path('csv_data/latest_data',f'{self.__name__}.csv')
    
    @classmethod
    def get_csv_backup_file_path(self):
        folder = f'csv_data/backup_data/{self.__name__}'
        file = f'{self.__name__}_{timezone.now().strftime("%Y%m%d%H%M%S")}.csv'
        return self.get_file_path(folder,file)
    
    @classmethod
    def get_csv_upload_file_path(self):
        return self.get_file_path('csv_data/upload_data',f'{self.__name__}.csv')
    
    @classmethod
    def back_up_existing(self):
        csv_latest_path = self.get_csv_latest_file_path()
        csv_backup_path = self.get_csv_backup_file_path()
        if os.path.isfile(csv_latest_path):
            shutil.copy(csv_latest_path, csv_backup_path)

    @classmethod
    def delete_existing(self):
        self.objects.all().delete()
        csv_latest_path = self.get_csv_latest_file_path()
        if os.path.isfile(csv_latest_path):
            os.remove(csv_latest_path)