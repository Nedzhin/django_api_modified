# management/commands/add_sample_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from core.models import GPSurgery, GP, Patient, InstructionType, Instruction

class Command(BaseCommand):
    help = 'Add sample data to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before adding new data',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            Instruction.objects.all().delete()
            Patient.objects.all().delete()
            GP.objects.all().delete()
            GPSurgery.objects.all().delete()
            InstructionType.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Data cleared!'))
        
        self.stdout.write(self.style.SUCCESS('Adding sample data...'))
        
        # Create GP Surgeries
        surgeries_data = [
            "City Medical Centre",
            "Riverside Health Practice",
            "Oakwood Family Practice",
            "Greenfield Medical Center"
        ]
        
        surgeries = []
        for surgery_name in surgeries_data:
            surgery, created = GPSurgery.objects.get_or_create(name=surgery_name)
            surgeries.append(surgery)
            if created:
                self.stdout.write(f'Created surgery: {surgery_name}')
        
        # Create GPs
        gps_data = [
            ("Dr. Sarah Smith", surgeries[0]),
            ("Dr. Michael Johnson", surgeries[0]),
            ("Dr. Emma Williams", surgeries[1]),
            ("Dr. David Brown", surgeries[1]),
            ("Dr. Lisa Davis", surgeries[2]),
            ("Dr. James Wilson", surgeries[3]),
        ]
        
        gps = []
        for gp_name, surgery in gps_data:
            gp, created = GP.objects.get_or_create(name=gp_name, surgery=surgery)
            gps.append(gp)
            if created:
                self.stdout.write(f'Created GP: {gp_name}')
        
        # Create Patients
        patients_data = [
            ("John", "Doe"),
            ("Jane", "Smith"),
            ("Bob", "Brown"),
            ("Alice", "Johnson"),
            ("Charlie", "Wilson"),
            ("Diana", "Davis"),
            ("Eve", "Miller"),
            ("Frank", "Taylor"),
        ]
        
        patients = []
        for first_name, last_name in patients_data:
            patient, created = Patient.objects.get_or_create(
                first_name=first_name, 
                last_name=last_name
            )
            patients.append(patient)
            if created:
                self.stdout.write(f'Created patient: {first_name} {last_name}')
        
        # Create Instruction Types
        instruction_types = []
        for choice in ['AMRA', 'SARS', 'POA', 'VAC']:
            inst_type, created = InstructionType.objects.get_or_create(name=choice)
            instruction_types.append(inst_type)
            if created:
                self.stdout.write(f'Created instruction type: {choice}')
        
        # Create Instructions
        import random
        base_date = datetime.now().date()
        
        for i in range(20):  # Create 20 sample instructions
            instruction, created = Instruction.objects.get_or_create(
                instruction_type=random.choice(instruction_types),
                patient=random.choice(patients),
                gp=random.choice(gps),
                surgery=random.choice(surgeries),
                date=base_date - timedelta(days=random.randint(0, 30))
            )
            if created:
                self.stdout.write(f'Created instruction: {instruction}')
        
        self.stdout.write(
            self.style.SUCCESS('Sample data added successfully!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total Instructions: {Instruction.objects.count()}')
        )




