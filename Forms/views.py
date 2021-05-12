from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import FormView

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'forms.html'
    success_url = '/'