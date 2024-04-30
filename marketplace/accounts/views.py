from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout

from .serializers import RegistrationSerializer
from django.views.decorators.http import require_POST

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            login(request, user)
            return JsonResponse({'message': 'User registered and logged in successfully'}, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
@require_POST
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'message': 'User logged in successfully'}, status=200)
    return JsonResponse({'error': 'Authentication failed'}, status=401)


@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully'}, status=200)
