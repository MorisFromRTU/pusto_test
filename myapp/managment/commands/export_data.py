from django.core.management.base import BaseCommand
from myapp.utils import export_player_level_data_to_csv

class Command(BaseCommand):
    help = 'Export player level data to CSV'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        export_player_level_data_to_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Successfully exported data to CSV'))
