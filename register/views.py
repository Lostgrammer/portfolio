from django.shortcuts import render
#registro de usuario
from django.contrib.auth.forms import UserCreationForm
#comparar datos de usuario
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    #condicional de que mostrar
    if request.method == 'GET':
        return render(request, "register.html", {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #en caso falle el registro en db
            try:
                # registrar usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado')
            except:
                return render(request, "register.html", {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, "register.html", {
            'form': UserCreationForm,
            'error': 'Las contras no coinciden'
        })


