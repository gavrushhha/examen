# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import UserSerializer

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }
    
    def test_create_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_user_str_representation(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data['username'])

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }

    def test_valid_user_serializer(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_user_serializer(self):
        invalid_user_data = self.user_data.copy()
        invalid_user_data['email'] = 'invalidemail'  # Invalid email
        serializer = UserSerializer(data=invalid_user_data)
        self.assertFalse(serializer.is_valid())

class UserRegistrationAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('user_registration')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }

    # def test_user_registration(self):
    #     response = self.client.post(self.register_url, self.user_data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertTrue(get_user_model().objects.filter(username=self.user_data['username']).exists())

class UserLoginAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('user_login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    # def test_user_login(self):
    #     response = self.client.post(self.login_url, self.user_data)
    #     self.assertEqual(response.status_code, 200)

    # def test_invalid_user_login(self):
    #     invalid_user_data = {
    #         'username': 'testuser',
    #         'password': 'wrongpassword'
    #     }
    #     response = self.client.post(self.login_url, invalid_user_data)
    #     self.assertEqual(response.status_code, 401)

class UserLogoutAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('user_logout')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    # def test_user_logout(self):
    #     self.client.login(username=self.user_data['username'], password=self.user_data['password'])
    #     response = self.client.post(self.logout_url)
    #     self.assertEqual(response.status_code, 200)

    # def test_user_logout_get(self):
    #     self.client.login(username=self.user_data['username'], password=self.user_data['password'])
    #     response = self.client.get(self.logout_url)
    #     self.assertEqual(response.status_code, 200)
