from django.shortcuts import render, redirect
from .models import Libro, Membro
from libreria.forms import LibroForm, MembroForm, CercaLibroForm, PrestaLibroForm


# Create your views here.

def libreria(request):
    form = None
    form = CercaLibroForm(request.GET or None)
    libri = Libro.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data['query'].lower()
        libri = [libro for libro in libri if query in libro.title.lower() or query in libro.author.lower() or query == libro.book_id]
    
    context = {'libri':libri, 'form': form}

    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/libreria-home.html', context)  



def lista_membri(request):
    libri = Libro.objects.all()
    membri = Membro.objects.all()
    context = {'libri':libri, 'membri':membri}
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/list-members.html', context)  





def libro(request, book):
    membri = Membro.objects.all()
    context = {'membri':membri, 'libro':book}
    if request.method == 'POST':
        if 'escludi' in request.POST:
            if book.is_expired:
                book.is_expired = False
                book.save()
            else:
                book.is_expired = True
                book.save()
        elif 'elimina' in request.POST:
            book.delete()
            return redirect('home')
        elif 'prenota' in request.POST:
            form = PrestaLibroForm(request.POST)
            if form.is_valid():
                member_id = form.cleaned_data['prenota']

    return render(request, 'libreria/libro.html', context) 



def membro(request, member):
    libri = Libro.objects.all()
    context = {'membro':member, 'libri':libri}
    if request.method == 'POST':
        if 'elimina' in request.POST:
            member.delete()
            return redirect('lista_membri')

    return render(request, 'libreria/membro.html', context)  





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
    
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  



def modifica_libro(request, book):
    context = {}
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')  # Reindirizza alla home dopo l'inserimento
    else:
        form = LibroForm()
    
    context['form'] = form
    
    libri = Libro.objects.all()
    context['libri'] = libri
    context['libro'] = book
    
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
    
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-member.html', context)  



def modifica_membro(request, member):
    context = {}
    if request.method == 'POST':
        form = MembroForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')  # Reindirizza alla home dopo l'inserimento
    else:
        form = MembroForm()
    
    context['form'] = form
    
    libri = Libro.objects.all()
    context['libri'] = libri
    context['membro'] = member

    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-member.html', context) 

