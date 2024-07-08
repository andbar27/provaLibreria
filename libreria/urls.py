from django.urls import path
from . import views
from .models import Libro, Membro

urlpatterns = [
    path('', views.libreria, name='home'),                                          # localhost:8000/libreria
    path('stats_libreria', views.statistiche_libreria, name='stats_library'), 
    path('add-book', views.aggiungi_libro, name='aggiungi_libro'),
    path('add-member', views.aggiungi_membro, name='aggiungi_membro'),
    path('list-members', views.lista_membri, name='lista_membri'),
    path('<str:book_id>', views.libro, name="book"),                                # The book details page
    path('<str:book_id>/modify', views.modifica_libro, name="book-modify"),         # The profile page
    path('m/<str:member_id>', views.membro, name="member"),                         # The profile page
    path('m/<str:member_id>/modify', views.modifica_membro, name="member-modify"),  # Edit profile page
    path('membro/<str:member_id>/return_book/<str:book_id>/', views.restituisci_libro, name='return_book'),
      
]
# for i in Libro.objects.all():
#     urlpatterns.append(path(i.book_id, views.libro, {"book":i}, name=i.book_id))
#     urlpatterns.append(path(i.book_id+"/modify", views.modifica_libro, {"book":i}, name=i.book_id + "-modify"))

# for j in Membro.objects.all():
#     urlpatterns.append(path("m"+j.member_id, views.membro, {"member":j}, name="m" + j.member_id))
#     urlpatterns.append(path("m"+j.member_id+"/modify", views.modifica_membro, {"member":j}, name="m" + j.member_id + "-modify"))

