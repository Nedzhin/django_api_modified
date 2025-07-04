from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Instruction, GP, GPSurgery, InstructionType, Patient
from datetime import date

class InstructionAPITest(TestCase):
    def setUp(self):
        # Create test data
        self.surgery = GPSurgery.objects.create(name="Test Surgery")
        self.gp = GP.objects.create(name="Dr. Smith", surgery=self.surgery)
        self.patient = Patient.objects.create(first_name="John", last_name="Doe")
        self.instruction_type = InstructionType.objects.create(name="AMRA")
        
        self.instruction = Instruction.objects.create(
            instruction_type=self.instruction_type,
            patient=self.patient,
            gp=self.gp,
            date=date(2024, 1, 15)
        )

        # self.client = APIClient()
        # surgery = GPSurgery.objects.create(name="North Clinic")
        # gp = GP.objects.create(name="Dr. Khan", surgery=surgery)
        # patient = Patient.objects.create(first_name="John", last_name="Doe")
        # itype = InstructionType.objects.create(name="Referral")
        # Instruction.objects.create(gp=gp, patient=patient, instruction_type=itype, surgery=surgery, date="2024-02-01")
    def test_list_instructions_for_surgery(self):
        url = reverse('instruction-list', kwargs={'surgery_id': self.surgery.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['surgery'], "Test Surgery")
        
        instruction_data = response.data['instructions'][0]
        self.assertEqual(instruction_data['patient_full_name'], "John Doe")
        self.assertEqual(instruction_data['instruction_type_name'], "AMRA")
        self.assertEqual(instruction_data['gp_name'], "Dr. Smith")
    
    def test_filter_by_instruction_type(self):
        url = reverse('instruction-list', kwargs={'surgery_id': self.surgery.id})
        response = self.client.get(url, {'instruction_type': 'AMRA'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
    
    def test_invalid_surgery_id(self):
        url = reverse('instruction-list', kwargs={'surgery_id': 999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    # def test_instruction_list(self):
    #     response = self.client.get('/api/instructions/1/?instruction_type=Referral')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(response.json()) > 0)
