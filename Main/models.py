import uuid

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


class Producent(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Foto(models.Model):
    nazwa = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Fotografia"
        verbose_name_plural = "Fotografie"


class Supplement(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(max_length=3500)
    dostepnosc = models.CharField(max_length=50)
    cena = models.CharField(max_length=50)
    rodzaj_suplementu = models.CharField(max_length=50)
    pojemnosc_suplementu = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Suplement"
        verbose_name_plural = "Suplementy"


class Ocena(models.Model):
    opinia = models.TextField(default="Wpisz swoją opinię")
    nota = models.IntegerField(default=5, validators=[MinValueValidator(1),
                                                      MaxValueValidator(5)])
    suplement = models.ForeignKey(Supplement, on_delete=models.CASCADE,
                                  related_name='oceny')

    def __str__(self):
        return self.suplement

    class Meta:
        verbose_name = "Ocena"
        verbose_name_plural = "Oceny"


class Koszyk(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    klient = models.ForeignKey(User, on_delete=models.CASCADE)
    zamowione = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Koszyk"
        verbose_name_plural = "Koszyk"

    @property
    def kompletna_kwota(self):
        elementy_koszyka = self.cartitems.all()
        cena = sum([produkt.kwota for produkt in elementy_koszyka])
        return cena


class ElementKoszyka(models.Model):
    produkt = models.ForeignKey(Supplement, on_delete=models.CASCADE, related_name='items')
    koszyk = models.ForeignKey(Koszyk, on_delete=models.CASCADE, related_name='cartitems')
    ilosc = models.IntegerField(default=0)

    def __str__(self):
        return self.produkt.nazwa

    class Meta:
        verbose_name = "Element koszyka"
        verbose_name_plural = "Elementy koszyka"

    @property
    def kwota(self):
        cena = self.produkt.cena.split()
        nowa_cena = int(cena[0]) * self.ilosc
        return nowa_cena


class Zamowienie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    numer_telefonu = models.CharField(max_length=12)
    miasto = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)
    koszyk = models.ForeignKey(Koszyk, on_delete=models.CASCADE, related_name='cart')
    zamowione = models.BooleanField(default=False)
    kwota = models.FloatField(default=100)
    data = models.DateTimeField(auto_now_add=True)
    zrealizowane = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"


class KodyRabatowe(models.Model):
    nazwa = models.CharField(max_length=20)
    procent = models.FloatField(default=0.9)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Kod rabatowy"
        verbose_name_plural = "Kody rabatowe"
