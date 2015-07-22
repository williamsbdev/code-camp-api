from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=100)
