from django.urls import path
from . import views
from .models import Libro, Membro

urlpatterns = [
    path('', views.libreria, name='home'),                                          # localhost:8000/libreria
    path('stats_libreria', views.statistiche_libreria, name='stats_library'),       # Stats library page
    path('add-book', views.aggiungi_libro, name='aggiungi_libro'),                  # Add book page
    path('add-member', views.aggiungi_membro, name='aggiungi_membro'),              # Add member page
    path('list-members', views.lista_membri, name='lista_membri'),                  # List member page
    path('<str:book_id>', views.libro, name="book"),                                # The book details page
    path('<str:book_id>/modify', views.modifica_libro, name="book-modify"),         # Edit book page
    path('m/<str:member_id>', views.membro, name="member"),                         # The profile page
    path('m/<str:member_id>/modify', views.modifica_membro, name="member-modify"),  # Edit profile page
                                                                                    # Return book url
    path('membro/<str:member_id>/return_book/<str:book_id>/', views.restituisci_libro, name='return_book'),
      
]
# for i in Libro.objects.all():
#     urlpatterns.append(path(i.book_id, views.libro, {"book":i}, name=i.book_id))
#     urlpatterns.append(path(i.book_id+"/modify", views.modifica_libro, {"book":i}, name=i.book_id + "-modify"))

# for j in Membro.objects.all():
#     urlpatterns.append(path("m"+j.member_id, views.membro, {"member":j}, name="m" + j.member_id))
#     urlpatterns.append(path("m"+j.member_id+"/modify", views.modifica_membro, {"member":j}, name="m" + j.member_id + "-modify"))

