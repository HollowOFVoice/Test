from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/login/'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'