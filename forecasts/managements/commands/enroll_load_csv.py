# forecasts/management/commands/load_csv.py
import os
import shutil
import pandas as pd
from django.core.management.base import BaseCommand
from forecasts.models import Enroll
from datetime import datetime

class Command(BaseCommand):
    help = 'Load data from CSV into the Enroll model'

    def handle(self, *args, **options):
        # Change 'data.csv' to your actual CSV file name
        csv_file_path = 'data.csv'

        # Create a backup with a timestamp
        backup_folder = 'backups'
        os.makedirs(backup_folder, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file_path = os.path.join(backup_folder, f'backup_{timestamp}.csv')
        shutil.copy2(csv_file_path, backup_file_path)

        self.stdout.write(self.style.SUCCESS(f'Backup created: {backup_file_path}'))

        # Load data from CSV into the Enroll model
        df = pd.read_csv(csv_file_path, iterator=True, chunksize=1000)  # Adjust chunk size based on your memory constraints

        Enroll.objects.all().delete()  # Clear existing data

        for chunk in df:
            records = chunk.to_dict('records')
            Enroll.objects.bulk_create([Enroll(**record) for record in records])

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
