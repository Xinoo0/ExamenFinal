from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, ContactoForm
from django.contrib.auth import authenticate, login
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request,'core/about.html')

def formulario(request):
    data = {'form': ContactoForm}
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'core/formulario.html')

def API(request):
    return render(request, 'core/API.html')

def products(request):
    return render(request, 'core/products.html')

# FUNCIONES LOGIN

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html',data)

# FUNCIONES CRUD

@staff_member_required
def crud(request):
    pro=Producto.objects.all()
    return render(request,'core/crud.html',{'pro':pro})

def agregar(request):
    return render(request,'core/agregar.html')

def agregarrec(request):
    x=request.POST['producto']
    y=request.POST['descripcion']
    z=request.POST['precio']
    pro=Producto(producto=x,descripcion=y,precio=z)
    pro.save()
    return redirect("/")

def eliminar(request,id):
    pro=Producto.objects.get(id=id)
    pro.delete()
    return redirect("/")

def actualizar(request,id):
    pro=Producto.objects.get(id=id)
    return render(request,'core/actualizar.html',{'pro':pro})

def actualizarrec(request,id):
    x=request.POST['producto']
    y=request.POST['descripcion']
    z=request.POST['precio']
    pro=Producto.objects.get(id=id)
    pro.producto=x
    pro.descripcion=y
    pro.precio=z
    pro.save()
    return redirect("/")
