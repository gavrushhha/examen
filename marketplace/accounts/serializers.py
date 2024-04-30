from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password1']
        if password != validated_data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        user = User.objects.create_user(username=username, password=password)
        return user
