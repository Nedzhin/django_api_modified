from rest_framework import serializers
from .models import Instruction, Patient, GP, GPSurgery, InstructionType

# Patient serializer to include full name
class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'full_name']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
class GPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GP
        fields = ['id', 'name']

class InstructionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionType
        fields = ['id', 'name']

class GPSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSurgery
        fields = ['id', 'name']

class InstructionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    gp = GPSerializer(read_only=True)
    instruction_type = InstructionTypeSerializer(read_only=True)
    surgery = GPSurgerySerializer(read_only=True)
    
    class Meta:
        model = Instruction
        fields = ['id', 'patient', 'gp', 'instruction_type', 'surgery', 'date']
