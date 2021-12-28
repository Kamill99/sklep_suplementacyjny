from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Supplement(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(max_length=250)
    dostepnosc = models.CharField(max_length=50)
    cena = models.CharField(max_length=50)
    rodzaj_suplementu = models.CharField(max_length=50)
    pojemnosc_suplementu = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Ocena(models.Model):
    opinia = models.TextField(default="Wpisz swoją opinię")
    nota = models.IntegerField(default=5, validators=[MinValueValidator(1),
                                                      MaxValueValidator(5)])
    suplement = models.ForeignKey(Supplement, on_delete=models.CASCADE,
                                  related_name='oceny')
