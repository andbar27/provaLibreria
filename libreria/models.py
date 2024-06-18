from django.db import models

# Create your models here.

class Libro(models.Model):
    book_id = models.CharField(max_length=13)
    image = models.ImageField()
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    is_borrowed = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.title
    
class Membro(models.Model):
    member_id = models.CharField(max_length=13)
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name