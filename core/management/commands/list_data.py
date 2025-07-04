# management/commands/list_data.py
from django.core.management.base import BaseCommand
from core.models import GPSurgery, GP, Patient, InstructionType, Instruction

class Command(BaseCommand):
    help = 'List all data in the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== DATABASE CONTENTS ==='))
        
        # List GP Surgeries
        self.stdout.write(self.style.HTTP_INFO('\nGP Surgeries:'))
        for surgery in GPSurgery.objects.all():
            self.stdout.write(f'  - {surgery.id}: {surgery.name}')
        
        # List GPs
        self.stdout.write(self.style.HTTP_INFO('\nGPs:'))
        for gp in GP.objects.all():
            self.stdout.write(f'  - {gp.id}: {gp.name} (Surgery: {gp.surgery.name})')
        
        # List Patients
        self.stdout.write(self.style.HTTP_INFO('\nPatients:'))
        for patient in Patient.objects.all():
            self.stdout.write(f'  - {patient.id}: {patient.first_name} {patient.last_name}')
        
        # List Instruction Types
        self.stdout.write(self.style.HTTP_INFO('\nInstruction Types:'))
        for inst_type in InstructionType.objects.all():
            self.stdout.write(f'  - {inst_type.id}: {inst_type.name}')
        
        # List Instructions
        self.stdout.write(self.style.HTTP_INFO('\nInstructions:'))
        for instruction in Instruction.objects.all()[:10]:  # Show first 10
            self.stdout.write(f'  - {instruction.id}: {instruction}')
        
        if Instruction.objects.count() > 10:
            self.stdout.write(f'  ... and {Instruction.objects.count() - 10} more')
        
        self.stdout.write(self.style.SUCCESS(f'\nTotal records: {Instruction.objects.count()} instructions'))
