# Generated by Django 5.0.6 on 2024-07-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_remove_libro_id_alter_libro_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='id',
        ),
        migrations.AlterField(
            model_name='membro',
            name='member_id',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
