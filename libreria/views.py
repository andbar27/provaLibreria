from django.shortcuts import render, redirect
from .models import Libro, Membro
from libreria.forms import LibroForm, MembroForm

# Create your views here.

def libreria(request):
    libri = Libro.objects.all()
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/libreria-home.html', {'libri':libri})  

def libro(request, book):
    if request.method == 'POST':
        if book.is_borrowed:
            book.is_borrowed = False
            book.save()
        else:
            book.is_borrowed = True
            book.save()

    return render(request, 'libreria/libro.html', {'libro':book})  

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

def aggiungi_membro(request):
    context = {}
    if request.method == 'POST':
        form = MembroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Reindirizza alla home dopo l'inserimento
    else:
        form = MembroForm()
    
    context['form'] = form
    
    membri = Membro.objects.all()
    context['membri'] = membri
    
    print(form) 
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-member.html', context)  

