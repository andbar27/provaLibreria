from django import forms
from libreria.models import Libro

"""class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['book_id', 'image', 'title', 'author', 'is_borrowed', 'is_expired']"""

class LibroForm(forms.Form):
    book_id = forms.CharField(label="book_id", max_length=13)
    image = forms.ImageField(label="image")
    title = forms.CharField(label="title", max_length=40)
    author = forms.CharField(label="author", max_length=40)
    is_borrowed = forms.BooleanField(label="is_borrowed")
    is_expired = forms.BooleanField(label="is_expired")