from django.shortcuts import render
#registro de usuario
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    return render(request, "register.html")