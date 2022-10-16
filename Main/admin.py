from django.contrib import admin
from .models import Supplement, Ocena, Producent, Kategoria, Foto, Koszyk, ElementKoszyka

admin.site.register(Supplement)
admin.site.register(Ocena)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Foto)
admin.site.register(ElementKoszyka)
admin.site.register(Koszyk)
