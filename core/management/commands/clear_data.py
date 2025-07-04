# management/commands/clear_data.py
from django.core.management.base import BaseCommand
from core.models import GPSurgery, GP, Patient, InstructionType, Instruction

class Command(BaseCommand):
    help = 'Clear all data from the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm deletion without prompting',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            confirm = input('Are you sure you want to delete ALL data? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.ERROR('Operation cancelled'))
                return
        
        self.stdout.write(self.style.WARNING('Clearing all data...'))
        
        # Delete in reverse order of dependencies
        deleted_counts = {}
        deleted_counts['Instructions'] = Instruction.objects.all().delete()[0]
        deleted_counts['Patients'] = Patient.objects.all().delete()[0]
        deleted_counts['GPs'] = GP.objects.all().delete()[0]
        deleted_counts['GP Surgeries'] = GPSurgery.objects.all().delete()[0]
        deleted_counts['Instruction Types'] = InstructionType.objects.all().delete()[0]
        
        self.stdout.write(self.style.SUCCESS('Data cleared successfully!'))
        for model, count in deleted_counts.items():
            self.stdout.write(f'  - {model}: {count} records deleted')