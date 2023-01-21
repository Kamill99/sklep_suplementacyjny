from django.contrib import admin
from .models import Suplement, Producent, Kategoria, Foto, Koszyk, ElementKoszyka, Zamowienie, KodyRabatowe

admin.site.register(Suplement)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Foto)
admin.site.register(ElementKoszyka)
admin.site.register(Koszyk)
admin.site.register(Zamowienie)
admin.site.register(KodyRabatowe)
