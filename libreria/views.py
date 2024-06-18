from django.shortcuts import render
from .models import Libro
from libreria.froms import LibroForm

# Create your views here.

def libreria(request):
    libri = Libro.objects.all()
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/libreria-home.html', {'libri':libri})  


def aggiungi_libro(request):
    context = {}
    libri = Libro.objects.all()
    form = LibroForm()
    context['libri'] = libri
    if request.method == 'POST':
        if 'save' in request.POST:
            form = LibroForm(request.POST)
            form.save()
    context['form'] = form
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  

