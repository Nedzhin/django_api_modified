from django.db import models

INSTRUCTION_TYPE_CHOICES = (
    ("AMRA", "AMRA"),
    ("SARS", "SARS"),
    ("POA", "POA"),
    ("VAC", "VACCINE"),
)

class GPSurgery(models.Model):
    name = models.CharField(max_length=255)

class GP(models.Model):
    name = models.CharField(max_length=255)
    surgery = models.ForeignKey(GPSurgery, on_delete=models.CASCADE)

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class InstructionType(models.Model):
    name = models.CharField(max_length=4, choices=INSTRUCTION_TYPE_CHOICES)

class Instruction(models.Model):
    instruction_type = models.ForeignKey(InstructionType, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    gp = models.ForeignKey(GP, on_delete=models.CASCADE)
    surgery = models.ForeignKey(GPSurgery, on_delete=models.CASCADE)
    date = models.DateField()