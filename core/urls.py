from django.urls import path
from .views import home, about, products, formulario, API, register, crud
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('products/', products,name='products'),
    path('formulario/', formulario, name='formulario'),
    path('API/', API, name='API'),
    path('register/', register, name='register'),
    path('crud/', views.crud, name='crud'),
    path('agregar/',views.agregar, name='agregar'),
    path('agregarrec/',views.agregarrec,name='agregarrec'),
    path('crud/eliminar/<int:id>/', views.eliminar,name='eliminar'),
    path('crud/actualizar/<int:id>/',views.actualizar,name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/',views.actualizarrec,name='actualizarrec')
]