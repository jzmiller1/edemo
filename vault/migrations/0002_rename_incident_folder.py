# Generated by Django 4.1.5 on 2023-01-10 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incident',
            new_name='Folder',
        ),
    ]