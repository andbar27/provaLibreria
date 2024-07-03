from django import forms
from .models import Libro, Membro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['book_id', 'image', 'title', 'author', 'is_borrowed', 'is_expired']

class LibroFormEdit(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['book_id', 'image', 'title', 'author', 'is_borrowed', 'is_expired']
        
    def __init__(self, *args, **kwargs):
        super(LibroFormEdit, self).__init__(*args, **kwargs)
        self.fields['book_id'].disabled = True


class MembroForm(forms.ModelForm):

    class Meta:
        model = Membro
        fields = ['member_id', 'name']