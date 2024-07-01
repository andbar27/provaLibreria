from django.urls import path
from . import views
from .models import Libro

urlpatterns = [
    # localhost:8000/libreria
    path('', views.libreria, name='home'),
    path('add-book', views.aggiungi_libro, name='aggiungi_libro'),
    path('add-member', views.aggiungi_membro, name='aggiungi_membro'),
    #path('profile/<str:username>/', views.membro),  # The profile page
]
for i in Libro.objects.all():
    urlpatterns.append(path(i.book_id, views.libro, {"book":i}, name=i.title.replace(" ","%20")))

