from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import json

# Function to generate JWT tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# ✅ Class-based LoginView
class LoginView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = authenticate(username=email, password=password)
            if user is not None:
                tokens = get_tokens_for_user(user)
                return Response({
                    "token": tokens["access"],
                    "user": {
                        "id": user.id,
                        "name": user.get_full_name(),
                        "role": "employee"
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)

# ✅ Class-based RegisterView
class RegisterView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get("email")
            username = email  # Use email as username
            password = data.get("password")

            if User.objects.filter(email=email).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)
