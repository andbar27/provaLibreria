from django import forms
from .models import Libro, Membro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['book_id', 'image', 'title', 'author', 'is_borrowed', 'is_expired']


class MembroForm(forms.ModelForm):

    class Meta:
        model = Membro
        fields = ['member_id', 'name']


class CercaLibroForm(forms.Form):

    query = forms.CharField(label='Cerca libro', max_length=40)


class PrestaLibroForm(forms.Form):

    membro_id = forms.CharField(label="Prenota", max_length=13)
