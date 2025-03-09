from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Membro
from libreria.forms import LibroForm, MembroForm, CercaLibroForm, AssegnaLibroForm, PasswordForm
from django.templatetags.static import static
from django.conf import settings

password = settings.LIBRERIA_PASSWORD

def libreria(request):
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





def libro(request, book_id):
    book = get_object_or_404(Libro, book_id=book_id)
    membri = Membro.objects.all().order_by("name")
    context = {'membri':membri, 'libro':book}
    form = AssegnaLibroForm(instance=book)
    if request.method == 'POST':
        if 'escludi' in request.POST:
            if book.is_expired:
                book.is_expired = False
                book.save()
            else:
                book.is_expired = True
                book.member = None
                book.is_borrowed = False
                book.save()

        elif 'elimina' in request.POST:
            book.delete()
            return redirect('home')
        
        elif 'prenota' in request.POST:
            if not book.is_expired:
                form = AssegnaLibroForm(request.POST, instance=book) #se voglio conservarlo posso metterlo sopra l'if
                if form.is_valid():
                    form.save()
                    book.is_borrowed = True
                    book.save()
                    return redirect('book', book_id) #se non ci fosse il form prima degli if non passeremmo al context form 
        else: 
            form = AssegnaLibroForm(instance=book)

    context['form'] = form
    return render(request, 'libreria/libro.html', context) 



def restituisci_libro(request, member_id, book_id):
    libro = get_object_or_404(Libro, book_id=book_id, member_id=member_id)
    libro.member = None
    libro.is_borrowed = False
    libro.save()
    return redirect("member", member_id)



def aggiungi_libro(request):
    context = {}
    form = LibroForm()
    password_form = PasswordForm()  # Assicuriamoci che esista anche per una richiesta GET
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        password_form = PasswordForm(request.POST or None)
        if form.is_valid() and password_form.is_valid():
            if 'image' not in request.FILES:
                libro.image = static('libreria/libro.png')
            if password_form.cleaned_data.get('password', "") == password:
                form.save()
                return redirect('home')  # Reindirizza alla home dopo l'inserimento
    
    context['form'] = form
    context['password_form'] = password_form
    libri = Libro.objects.all()
    context['libri'] = libri
    
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  



def modifica_libro(request, book_id):
    book = get_object_or_404(Libro, book_id=book_id)
    context = {}
    form = LibroForm(instance=book)
    password_form = PasswordForm()  # Assicuriamoci che esista anche per una richiesta GET
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=book)
        password_form = PasswordForm(request.POST or None)
        if form.is_valid() and password_form.is_valid():
            if password_form.cleaned_data.get('password', "") == password:
                form.save()
                return redirect('home')  # Reindirizza alla home dopo l'inserimento
    
    context['form'] = form
    context['password_form'] = password_form
    libri = Libro.objects.all()
    context['libri'] = libri
    context['libro'] = book
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-book.html', context)  





def membro(request, member_id):
    member = get_object_or_404(Membro, member_id=member_id)
    libri = member.books.all()
    context = {'membro':member, 'libri':libri}
    if request.method == 'POST':
        if 'elimina' in request.POST:
            for libro in libri:
                libro.is_borrowed=False
                libro.save()
            member.delete()
            return redirect('lista_membri')

            
    return render(request, 'libreria/membro.html', context)  



def aggiungi_membro(request):
    context = {}
    password_form = PasswordForm()  # Assicuriamoci che esista anche per una richiesta GET

    if request.method == 'POST':
        form = MembroForm(request.POST, request.FILES)
        password_form = PasswordForm(request.POST or None)
        if form.is_valid() and password_form.is_valid():
            if password_form.cleaned_data.get('password', "") == password:
                form.save()
                return redirect('home')  # Reindirizza alla home dopo l'inserimento
    else:
        form = MembroForm() #passare nel context un bool per fare pop up in caso di errore
    
    context['form'] = form
    context['password_form'] = password_form
    membri = Membro.objects.all()
    context['membri'] = membri
    
    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-member.html', context)  



def modifica_membro(request, member_id):
    member = get_object_or_404(Membro, member_id=member_id)
    context = {}
    password_form = PasswordForm()  # Assicuriamoci che esista anche per una richiesta GET
    if request.method == 'POST':
        form = MembroForm(request.POST, request.FILES, instance=member)
        password_form = PasswordForm(request.POST or None)
        if form.is_valid() and password_form.is_valid():
            if password_form.cleaned_data.get('password', "") == password:
                form.save()
                return redirect('member', member_id=member_id)  # 
    else:
        form = MembroForm()
    
    context['form'] = form
    context['password_form'] = password_form
    libri = Libro.objects.all()
    context['libri'] = libri
    context['membro'] = member

    # 2°arg = percorso file  html
    # mettere file html in proj/app/templates/app 
    return render(request, 'libreria/add-member.html', context) 





def statistiche_libreria(request):

    members = list(Membro.objects.all())
    books = list(Libro.objects.all())
    n_members = len(members)
    n_books = len(books)
    books_borrowed = [libro for libro in books if libro.is_borrowed]
    books_expired = [libro for libro in books if libro.is_expired]

    context = {'membri':members, 'libri':books, 'n_membri':n_members, 'n_libri':n_books, 'libri_prestati':books_borrowed, 'n_libri_prestati':len(books_borrowed)}
    context['libri_scaduti'] = books_expired
    context['n_libri_scaduti'] =len(books_expired)
    return render(request, 'libreria/stats_libreria.html', context)
    