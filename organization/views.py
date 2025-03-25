from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Requires login token
def organization_dashboard(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response({"employees": serializer.data})
