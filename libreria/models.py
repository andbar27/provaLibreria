from typing import Any
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Membro(models.Model):
    member_id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class Libro(models.Model):
    book_id = models.CharField(max_length=13, validators=[MinLengthValidator(13)], primary_key=True)
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    is_borrowed = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    
    member = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')

    def __str__(self) -> str:
        return self.title
    
    def getUrl(self):
        return self.book_id
    

