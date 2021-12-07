from django.db import models

class Supplement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    available = models.BooleanField()
