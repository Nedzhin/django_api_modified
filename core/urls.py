from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
urlpatterns = [
    path('api/surgeries/<int:surgery_pk>/instructions/', 
         views.SurgeryInstructionViewSet.as_view({'get': 'list'}), 
         name='surgery-instructions'),
]