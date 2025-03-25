from django.urls import path
from .views import organization_dashboard, employee_dashboard  # Import both views

urlpatterns = [
    path('dashboard/', organization_dashboard, name='organization_dashboard'),  # Existing route
    path('employee/<int:id>/', employee_dashboard, name='employee_dashboard'),  # New employee details route
]
