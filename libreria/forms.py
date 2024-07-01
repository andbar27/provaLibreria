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