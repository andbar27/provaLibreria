from typing import Any
from django.db import models

# Create your models here.

class Libro(models.Model):
    book_id = models.CharField(max_length=13)
    print("aoooo: ", book_id)
    image = models.ImageField()
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    is_borrowed = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print("1")
        fields = ['book_id', 'image', 'title', 'author', 'is_borrowed', 'is_expired']
        for field in fields:
            if field not in kwargs:
                return
        print("2")
        book_id = kwargs['book_id']
        image = kwargs['image']
        title = kwargs['title']
        author = kwargs['author']
        is_borrowed = kwargs['is_borrowed']
        is_expired = kwargs['is_expired']
        print("3")

    def __str__(self) -> str:
        return self.title
    
class Membro(models.Model):
    member_id = models.CharField(max_length=13)
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name