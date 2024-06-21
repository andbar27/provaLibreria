from django.shortcuts import render
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
    form = LibroForm()
    # if request.method == 'POST':
    #     if "save" in request.POST:
    print("bellaaaaaa")
    form = LibroForm(request.POST)
    #if form.is_valid():
    book_id = form['book_id']
    image = form['image']
    title = form['title']
    author = form['author']
    is_borrowed = form['is_borrowed']
    is_expired = form['is_expired']
    Libro(book_id=book_id, image=image, title=title,author=author,is_borrowed=is_borrowed,is_expired=is_expired).save()
    libri = Libro.objects.all()
    context['libri'] = libri
    print("ciaoooooooo: ", image)


    context['form'] = form
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  

