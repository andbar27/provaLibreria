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


class AssegnaLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['member']

    member = forms.ModelChoiceField(queryset=Membro.objects.all(), label="Membro")
