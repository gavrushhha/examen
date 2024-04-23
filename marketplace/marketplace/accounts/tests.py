from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user

class AuthenticationTestCase(TestCase):
    
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.dashboard_url = '/home/'  # Assuming LOGIN_REDIRECT_URL is set to '/home/'
    
    def test_login(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': self.password}, follow=True)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, self.dashboard_url)

    def test_logout(self):
        # Login the user
        self.client.post(self.login_url, {'username': self.username, 'password': self.password})
        # Logout the user
        response = self.client.get(reverse('accounts:logout'), follow=True)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        # Assert redirection if needed
        # self.assertRedirects(response, reverse('base'))  # Assuming LOGIN
