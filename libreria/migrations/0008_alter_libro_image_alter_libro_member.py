# Generated by Django 5.1.6 on 2025-02-25 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0007_libro_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='image',
            field=models.ImageField(blank=True, default='./static/libreria/libro.png', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='libreria.membro'),
        ),
    ]
