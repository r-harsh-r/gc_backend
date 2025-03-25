from django.urls import path
from .views import organization_dashboard

urlpatterns = [
    path('dashboard/', organization_dashboard, name='organization_dashboard'),
]
