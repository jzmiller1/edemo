from django.db import models
from incidents.models import Incident as Record


class Folder(models.Model):
    name = models.CharField(max_length=10)
    incidents = models.ManyToManyField(
        Record,
        related_name='vault_incidents',
        blank=True
    )
