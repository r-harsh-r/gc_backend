from django.contrib.auth import authenticate
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = authenticate(username=email, password=password)

            if user is not None:
                tokens = get_tokens_for_user(user)
                return JsonResponse({
                    "token": tokens["access"],
                    "user": {
                        "id": user.id,
                        "name": user.get_full_name(),
                        "role": "employee"
                    }
                })
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
