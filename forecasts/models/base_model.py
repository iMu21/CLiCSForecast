from django.utils import timezone
import shutil
from django.db import models
import csv
import os

class BaseModel(models.Model):
    clics_db_id = models.IntegerField()

    class Meta:
        abstract = True  

    @classmethod
    def bulk_upload(self):
        self.back_up_existing()
        self.delete_existing()
        self.upload_data()
        self.export_model_to_csv()

    @classmethod
    def upload_data(self):
        csv_upload_path = self.get_csv_upload_file_path()
        with open(csv_upload_path, 'r', encoding='utf-8-sig') as csv_file: 
            reader = csv.DictReader(csv_file)
            chunks = []
            for row in reader:
                obj = self(**row)
                chunks.append(obj)
                if len(chunks)>1000:
                    self.objects.bulk_create(chunks)
                    chunks = []
            if len(chunks)>0:
                self.objects.bulk_create(chunks)

    @classmethod
    def export_model_to_csv(self):
        csv_latest_path = self.get_csv_latest_file_path()
        
        field_names = [field.name for field in self._meta.get_fields()]

        with open(csv_latest_path, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(field_names)
            for obj in self.objects.all():
                row_values = [str(getattr(obj, field)) for field in field_names]
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