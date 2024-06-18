from django.shortcuts import render
from .models import Libro
from libreria.forms import LibroForm

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
        form = LibroForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data["book_id"]
            image = form.cleaned_data["image"]
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            is_borrowed = form.cleaned_data["is_borrowed"]
            is_expired = form.cleaned_data["is_expired"]
            print("autor: ", author)


    context['form'] = form
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  

