from django.urls import path
from . import views
from .models import Libro, Membro

urlpatterns = [
    # localhost:8000/libreria
    path('', views.libreria, name='home'),
    path('add-book', views.aggiungi_libro, name='aggiungi_libro'),
    path('add-member', views.aggiungi_membro, name='aggiungi_membro'),
    path('list-members', views.lista_membri, name='lista_membri'),
    #path('profile/<str:username>/', views.membro),  # The profile page
    path('membro/<str:member_id>/return_book/<str:book_id>/', views.restituisci_libro, name='return_book'),
]
for i in Libro.objects.all():
    urlpatterns.append(path(i.book_id, views.libro, {"book":i}, name=i.title.replace(" ","%20")))
    urlpatterns.append(path(i.book_id+"/modify", views.modifica_libro, {"book":i}, name=i.title.replace(" ","%20") + "-modify"))

for j in Membro.objects.all():
    urlpatterns.append(path("m"+j.member_id, views.membro, {"member":j}, name=j.name.replace(" ","%20")))
    urlpatterns.append(path("m"+j.member_id+"/modify", views.modifica_membro, {"member":j}, name=j.name.replace(" ","%20") + "-modify"))

