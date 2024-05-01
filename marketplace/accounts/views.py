from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout


from accounts.forms import RegistrationForm
from accounts.models import Client

from accounts.serializers import ClientSerializer


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

    def get(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
