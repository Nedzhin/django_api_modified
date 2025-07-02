from django.test import TestCase
from rest_framework.test import APIClient
from .models import Instruction, GP, GPSurgery, InstructionType, Patient

class InstructionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        surgery = GPSurgery.objects.create(name="North Clinic")
        gp = GP.objects.create(name="Dr. Khan", surgery=surgery)
        patient = Patient.objects.create(first_name="John", last_name="Doe")
        itype = InstructionType.objects.create(name="Referral")
        Instruction.objects.create(gp=gp, patient=patient, instruction_type=itype, surgery=surgery, date="2024-02-01")

    def test_instruction_list(self):
        response = self.client.get('/api/instructions/1/?instruction_type=Referral')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
