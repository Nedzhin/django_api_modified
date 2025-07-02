from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Instruction
from .serializers import InstructionSerializer
from django.utils.dateparse import parse_date

class InstructionListView(APIView):
    def get(self, request, surgery_id):
        instructions = Instruction.objects.filter(surgery_id=surgery_id)

        instruction_type = request.GET.get('instruction_type')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if instruction_type:
            instructions = instructions.filter(instruction_type__name__iexact=instruction_type)
        if start_date:
            instructions = instructions.filter(date__gte=parse_date(start_date))
        if end_date:
            instructions = instructions.filter(date__lte=parse_date(end_date))

        serializer = InstructionSerializer(instructions, many=True)
        return Response(serializer.data)
