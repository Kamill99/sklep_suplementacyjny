from django.urls import include, path
from rest_framework import routers
from Main import views
from Main.views import *
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path('', index, name='index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('suplement/<id>', suplement, name='supplement'),
    path('rejestracja/', views.stronaRejestracji, name="rejestracja"),
    path('login/', views.stronaLogowania, name="login"),
    path('wylogowanie/', views.wylogowanie, name="wylogowanie"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
