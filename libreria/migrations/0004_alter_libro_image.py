# Generated by Django 5.0.6 on 2024-06-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_libro_author_alter_libro_book_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]