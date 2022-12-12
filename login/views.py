from django.shortcuts import render
#registro de usuario
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logine(request):
    return render(request, "logine.html")