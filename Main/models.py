from django.db import models


class Supplement(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(max_length=250)
    dostepnosc = models.CharField(max_length=50)
    cena = models.CharField(max_length=50)
    rodzaj_suplementu = models.CharField(max_length=50)
    pojemnosc_suplementu = models.CharField(max_length=50)
