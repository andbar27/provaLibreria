from django.urls import path
from . import views
from .models import Libro

urlpatterns = [
    # localhost:8000/libreria
    path('', views.libreria, name='home'),
    path('aggiungi_libro', views.aggiungi_libro, name='aggiungi_libro'),
]
for i in Libro.objects.all():
    urlpatterns.append(path(i.title.replace(" ","-").lower(), views.libro, {"book":i}, name=i.title.replace(" ","%20")))
    #+"<str:id="+str(i.book_id)">"