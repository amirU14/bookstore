from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

from .forms import CustomeUserCreationForm
class SignUpView(generic.CreateView):
    form_class = CustomeUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
