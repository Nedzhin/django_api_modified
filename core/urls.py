from django.urls import path
from .views import InstructionListView

urlpatterns = [
    path('api/instructions/<int:surgery_id>/', InstructionListView.as_view(), name='instruction-list'),
]
