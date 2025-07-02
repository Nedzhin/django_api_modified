from rest_framework import serializers
from .models import Instruction

class InstructionSerializer(serializers.ModelSerializer):
    patient_full_name = serializers.CharField(source='patient.full_name', read_only=True)
    instruction_type_name = serializers.CharField(source='instruction_type.name', read_only=True)
    gp_name = serializers.CharField(source='gp.name', read_only=True)

    class Meta:
        model = Instruction
        fields = ['id', 'patient_full_name', 'instruction_type_name', 'gp_name', 'date', 'surgery']
