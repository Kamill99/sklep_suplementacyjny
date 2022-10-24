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
    path('dodanie_do_koszyka/', views.dodanie_do_koszyka, name="dodanie_do_koszyka"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
