from django.shortcuts import render, redirect
from .models import Libro
from libreria.forms import LibroForm

# Create your views here.

def libreria(request):
    libri = Libro.objects.all()
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/libreria-home.html', {'libri':libri})  

def libro(request):
    libri = Libro.objects.all()
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/libro.html', {'libri':libri})  

def aggiungi_libro(request):
    context = {}
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Reindirizza alla home dopo l'inserimento
    else:
        form = LibroForm()
    
    context['form'] = form
    
    libri = Libro.objects.all()
    context['libri'] = libri
    
    print(form) 
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  

