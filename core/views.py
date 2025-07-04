from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
#from django.shortcuts import get_object_or_404
from .models import Instruction, GPSurgery
from .serializers import InstructionSerializer


class InstructionFilter(filters.FilterSet):
    instruction_type = filters.CharFilter(field_name='instruction_type__name')
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    
    class Meta:
        model = Instruction
        fields = ['instruction_type', 'start_date', 'end_date']


class SurgeryInstructionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to list all Instructions for a given GP Surgery.
    
    Supports filtering by:
    - instruction_type: Filter by instruction type (AMRA, SARS, POA, VAC)
    - start_date: Filter instructions from this date (YYYY-MM-DD)
    - end_date: Filter instructions up to this date (YYYY-MM-DD)
    
    Example URLs:
    - /api/surgeries/1/instructions/
    - /api/surgeries/1/instructions/?instruction_type=AMRA
    - /api/surgeries/1/instructions/?start_date=2024-01-01&end_date=2024-12-31
    """
    serializer_class = InstructionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InstructionFilter
    
    def get_queryset(self):
        surgery_id = self.kwargs['surgery_pk']
        # Verify surgery exists
        get_object_or_404(GPSurgery, pk=surgery_id)
        
        return Instruction.objects.filter(
            surgery_id=surgery_id
        ).select_related(
            'patient', 'gp', 'instruction_type', 'surgery'
        ).order_by('-date')
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })