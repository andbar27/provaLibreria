# Generated by Django 5.0.6 on 2024-06-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='immagine',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='prezzo',
        ),
        migrations.AddField(
            model_name='libro',
            name='author',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='libro',
            name='book_id',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='libro',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='libro',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='libro',
            name='title',
            field=models.CharField(default='', max_length=40),
        ),
    ]
