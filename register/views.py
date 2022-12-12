from django.shortcuts import render,redirect
#registro de usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#comparar datos de usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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
                login(request,user)
                return redirect('login')
            except:
                return render(request, "register.html", {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, "register.html", {
            'form': UserCreationForm,
            'error': 'Las contras no coinciden'
        })

#funcion para logearse
def loginn(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario no encontrado o contra invalida'
            })
        else:
            login(request,user)
            return redirect('index')
