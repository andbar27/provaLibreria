# Generated by Django 5.0.6 on 2024-06-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_membro_rename_immagine_libro_image_remove_libro_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='author',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='libro',
            name='book_id',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='libro',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
