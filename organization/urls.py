from django.urls import path
from .views import organization_dashboard, employee_dashboard

urlpatterns = [
    path('dashboard/', organization_dashboard, name='organization_dashboard'),  
    path('employee/<int:id>/', employee_dashboard, name='employee_dashboard'),  
]
