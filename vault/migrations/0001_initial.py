# Generated by Django 4.1.5 on 2023-01-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('incidents', models.ManyToManyField(blank=True, related_name='vault_incidents', to='incidents.incident')),
            ],
        ),
    ]
