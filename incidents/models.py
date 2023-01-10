from django.db import models


class Incident(models.Model):
    name = models.CharField(max_length=10)
