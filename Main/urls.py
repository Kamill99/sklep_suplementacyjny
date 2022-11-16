from rest_framework import routers
from Main import views
from Main.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', index, name='index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('szukaj/', views.szuakj, name='szukaj'),
    path('suplement/<id>', suplement, name='supplement'),
    path('profil/', profil, name='profil'),
    path('rejestracja/', views.strona_rejestracji, name="rejestracja"),
    path('login/', views.strona_logowania, name="login"),
    path('wylogowanie/', views.wylogowanie, name="wylogowanie"),
    path('edycja_profilu/', EdycjaProfilu.as_view(), name="edycja_profilu"),
    path('password/', PasswordsChangeView.as_view(template_name='zmiana_hasla.html')),
    path('zmienione_haslo/', views.zmienione_haslo, name="zmienione_haslo"),
    path('koszyk/', views.koszyk, name="koszyk"),
    path('brak_koszyka/', views.brak_koszyka, name="brak_koszyka"),
    path('dodanie_do_koszyka/', views.dodanie_do_koszyka, name="dodanie_do_koszyka"),
    path('aktualizacja_koszyka_plus/', views.aktualizacja_koszyka_plus, name="aktualizacja_koszyka_plus"),
    path('aktualizacja_koszyka_minus/', views.aktualizacja_koszyka_minus, name="aktualizacja_koszyka_minus"),
    path('usuwanie_elementu/', views.usuwanie_elementu, name="usuwanie_elementu"),
    path('pusty_koszyk/', views.pusty_koszyk, name="pusty_koszyk"),
    path('zamowienie/', views.zamowienie, name="zamowienie"),
    path('numer_telefonu/', views.numer_telefonu, name="numer_telefonu"),
    path('rozliczenie/', views.rozliczenie, name="rozliczenie"),
    path('udane_rozliczenie/', views.udane_rozliczenie, name="udane_rozliczenie"),
    path('podsumowanie/', views.podsumowanie, name="podsumowanie"),
    path('historia_zamowien/', views.historia_zamowien, name="historia_zamowien"),
    path('historia_zamowien/<id>', views.historia_zamowien_id, name="historia_zamowien_id"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
