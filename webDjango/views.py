from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .forms import Registro

def index(request):
    return render(request, 'index.html', {
        'mensaje': 'Tienda',
        'titulo' : 'Inicio',
        'productos' :[
            {'titulo': 'Campera','precio':15, 'stock':False},
            {'titulo':'Pantalon','precio':11, 'stock':True},
            {'titulo':'Remera','precio':18, 'stock':False},
            {'titulo':'Gorra','precio':10, 'stock' :True},
            ]
     })

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuarios=authenticate(username=username, password=password)
     
        if usuarios:
            lg(request, usuarios)
            messages.success(request, f'Bienvenido {usuarios.username}')
            return redirect('index')
        else:
            messages.error(request, 'Datos incorrectos')
           
    return render(request, 'users/login.html', {})

def salir(request): 
    logout(request) 
    messages.success(request, 'Sesión cerrada') 
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    form=Registro(request.POST or None)
    print(form.errors)
    if request.method=='POST' and form.is_valid():
        usuario=form.save()
        if usuario:
            lg(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Bienvenido')
            return redirect('index')
    return render(request, 'users/registro.html', {
        'form':form
        })
    
    

