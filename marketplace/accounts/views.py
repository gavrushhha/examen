from django.views.generic import CreateView

from .forms import RegistrationForm
from django.contrib.auth.models import User


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = '/'
    success_message = "User was created successfully"
