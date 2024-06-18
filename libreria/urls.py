from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/libreria
    path('', views.libreria, name='home'),
    path('aggiungi_libro', views.aggiungi_libro, name='aggiungi_libro'),
]