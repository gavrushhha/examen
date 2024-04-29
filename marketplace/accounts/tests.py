from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RegistrationForm


class FormTestCase(TestCase):
    def test_registration_form_valid(self):
        form_data = {
            'username': 'test_user',
            'password1': 'test_password',
            'password2': 'test_password',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            'username': 'test_user',
            'password1': 'test_password',
            'password2': 'different_password',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())