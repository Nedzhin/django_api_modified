from django.db import models

INSTRUCTION_TYPE_CHOICES = (
    ("AMRA", "AMRA"),
    ("SARS", "SARS"),
    ("POA", "POA"),
    ("VAC", "VACCINE"),
)

class GPSurgery(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "GP Surgeries"
    
class GP(models.Model):
    name = models.CharField(max_length=255)
    surgery = models.ForeignKey(GPSurgery, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    # for string display in admin
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class InstructionType(models.Model):
    name = models.CharField(max_length=4, choices=INSTRUCTION_TYPE_CHOICES)

    def __str__(self):
        return self.name
class Instruction(models.Model):
    instruction_type = models.ForeignKey(InstructionType, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    gp = models.ForeignKey(GP, on_delete=models.CASCADE)
    surgery = models.ForeignKey(GPSurgery, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.instruction_type.name} for {self.patient} on {self.date}"
    
    class Meta:
        ordering = ['-date']