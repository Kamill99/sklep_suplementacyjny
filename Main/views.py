import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from rest_framework.reverse import reverse_lazy
from .forms import PasswordChangingForm
from .models import Supplement, Kategoria, Koszyk, ElementKoszyka, Zamowienie, KodyRabatowe, Producent, Foto
from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from owlready2 import *
from django.views.decorators.cache import cache_control

quantity = tel_number = order_id = delivery_cost = 0
name = surname = city = post = delivery = payment = discount_code = ""

onto = get_ontology("Main/ontologia/suplementy.owl")
onto.load()
suplementy = []
ashwagandha = berberyna = cynk = kofeina = kolagen = luteina = magnez = melatonina = cbd = omega = rhodiola = \
    wapn = witamina_a = witamina_b = witamina_c = witamina_d = zelazo = None
trawienie_suplementy = koncentracja_suplementy = stres_suplementy = wegan_suplementy = \
    wegetarian_suplementy = pobudzenie_suplementy = stawy_suplementy = sen_suplementy = wzrok_suplementy = \
    pamiec_suplementy = odpornosc_suplementy = serce_suplementy = None
suplementy_klasa = []
ashwagandha_klasa = "untitled-ontology-15.Ashwagandha"
berberyna_klasa = "untitled-ontology-15.Berberyna"
cynk_klasa = "untitled-ontology-15.Cynk"
kofeina_klasa = "untitled-ontology-15.Kofeina-tabletki"
kolagen_klasa = "untitled-ontology-15.Kolagen"
luteina_klasa = "untitled-ontology-15.Luteina"
magnez_klasa = "untitled-ontology-15.Magnez"
melatonina_klasa = "untitled-ontology-15.Melatonina"
cbd_klasa = "untitled-ontology-15.Olejek_CBD"
omega_klasa = "untitled-ontology-15.Omega_3"
rhodiola_klasa = "untitled-ontology-15.Rhodiola_Rosea"
wapn_klasa = "untitled-ontology-15.Wapń"
witamina_a_klasa = "untitled-ontology-15.Witamina_A"
witamina_b_klasa = "untitled-ontology-15.Witamina_B12"
witamina_c_klasa = "untitled-ontology-15.Witamina_C"
witamina_d_klasa = "untitled-ontology-15.Witamina_D"
zelazo_klasa = "untitled-ontology-15.Żelazo"
suplementy_klasa.append(ashwagandha_klasa)
suplementy_klasa.append(berberyna_klasa)
suplementy_klasa.append(cynk_klasa)
suplementy_klasa.append(kofeina_klasa)
suplementy_klasa.append(kolagen_klasa)
suplementy_klasa.append(luteina_klasa)
suplementy_klasa.append(magnez_klasa)
suplementy_klasa.append(melatonina_klasa)
suplementy_klasa.append(cbd_klasa)
suplementy_klasa.append(omega_klasa)
suplementy_klasa.append(rhodiola_klasa)
suplementy_klasa.append(wapn_klasa)
suplementy_klasa.append(witamina_a_klasa)
suplementy_klasa.append(witamina_b_klasa)
suplementy_klasa.append(witamina_c_klasa)
suplementy_klasa.append(witamina_d_klasa)
suplementy_klasa.append(zelazo_klasa)
for klasa in onto.classes():
    if str(klasa) == ashwagandha_klasa:
        ashwagandha = klasa
        suplementy.append(ashwagandha)
    elif str(klasa) == berberyna_klasa:
        berberyna = klasa
        suplementy.append(berberyna)
    elif str(klasa) == cynk_klasa:
        cynk = klasa
        suplementy.append(cynk)
    elif str(klasa) == kofeina_klasa:
        kofeina = klasa
        suplementy.append(kofeina)
    elif str(klasa) == kolagen_klasa:
        kolagen = klasa
        suplementy.append(kolagen)
    elif str(klasa) == luteina_klasa:
        luteina = klasa
        suplementy.append(luteina)
    elif str(klasa) == magnez_klasa:
        magnez = klasa
        suplementy.append(magnez)
    elif str(klasa) == melatonina_klasa:
        melatonina = klasa
        suplementy.append(melatonina)
    elif str(klasa) == cbd_klasa:
        cbd = klasa
        suplementy.append(cbd)
    elif str(klasa) == omega_klasa:
        omega = klasa
        suplementy.append(omega)
    elif str(klasa) == rhodiola_klasa:
        rhodiola = klasa
        suplementy.append(rhodiola)
    elif str(klasa) == wapn_klasa:
        wapn = klasa
        suplementy.append(wapn)
    elif str(klasa) == witamina_a_klasa:
        witamina_a = klasa
        suplementy.append(witamina_a)
    elif str(klasa) == witamina_b_klasa:
        witamina_b = klasa
        suplementy.append(witamina_b)
    elif str(klasa) == witamina_c_klasa:
        witamina_c = klasa
        suplementy.append(witamina_c)
    elif str(klasa) == witamina_d_klasa:
        witamina_d = klasa
        suplementy.append(witamina_d)
    elif str(klasa) == zelazo_klasa:
        zelazo = klasa
        suplementy.append(zelazo)

wegan = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.DlaWegan)"
wegetarian = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.DlaWegetarian)"
koncentracja = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Koncentracja)"
sen = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.LepszySen)"
wzrok = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.OczyIWzrok)"
odpornosc = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Odporność)"
pamiec = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Pamięć)"
pobudzenie = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Pobudzenie)"
serce = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.PracaSerca)"
stawy = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Stawy)"
stres = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Stres)"
trawienie = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Trawienie)"


def index(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    witamina_c = Supplement.objects.get(id=1)
    witamina_d = Supplement.objects.get(id=37)
    zelazo = Supplement.objects.get(id=33)
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo,
            'witamina_c': witamina_c, 'witamina_d': witamina_d, 'zelazo': zelazo}
    return render(request, 'main.html', dane)


def kontakt(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'kontakt.html', dane)


def ankieta(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    if request.method == "POST":
        dieta_ankieta = request.POST.get('dieta')
        koncentracja_ankieta = request.POST.get('koncentracja')
        sen_ankieta = request.POST.get('sen')
        pamiec_ankieta = request.POST.get('pamiec')
        stres_ankieta = request.POST.get('stres')
        pobudzenie_ankieta = request.POST.get('pobudzenie')
        wzrok_ankieta = request.POST.get('wzrok')
        odpornosc_ankieta = request.POST.get('odpornosc')
        serce_ankieta = request.POST.get('serce')
        stawy_ankieta = request.POST.get('stawy')
        trawienie_ankieta = request.POST.get('trawienie')
        if dieta_ankieta == "wegan":
            global wegan_suplementy
            wegan_suplementy = []
            global wegan
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == wegan:
                        polecenie = str(suplement)
                        wegan_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            wegan_suplementy = None
        if dieta_ankieta == "wegetarian":
            global wegetarian_suplementy
            wegetarian_suplementy = []
            global wegetarian
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == wegetarian:
                        polecenie = str(suplement)
                        wegetarian_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            wegetarian_suplementy = None
        if koncentracja_ankieta == "koncentracja_tak":
            global koncentracja_suplementy
            koncentracja_suplementy = []
            global koncentracja
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == koncentracja:
                        polecenie = str(suplement)
                        koncentracja_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            koncentracja_suplementy = None
        if sen_ankieta == "sen_tak":
            global sen_suplementy
            sen_suplementy = []
            global sen
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == sen:
                        polecenie = str(suplement)
                        sen_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            sen_suplementy = None
        if pamiec_ankieta == "pamiec_tak":
            global pamiec_suplementy
            pamiec_suplementy = []
            global pamiec
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == pamiec:
                        polecenie = str(suplement)
                        pamiec_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            pamiec_suplementy = None
        if stres_ankieta == "stres_tak":
            global stres_suplementy
            stres_suplementy = []
            global stres
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == stres:
                        polecenie = str(suplement)
                        stres_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            stres_suplementy = None
        if pobudzenie_ankieta == "pobudzenie_tak":
            global pobudzenie_suplementy
            pobudzenie_suplementy = []
            global pobudzenie
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == pobudzenie:
                        polecenie = str(suplement)
                        pobudzenie_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            pobudzenie_suplementy = None
        if wzrok_ankieta == "wzrok_tak":
            global wzrok_suplementy
            wzrok_suplementy = []
            global wzrok
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == wzrok:
                        polecenie = str(suplement)
                        wzrok_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            wzrok_suplementy = None
        if odpornosc_ankieta == "odpornosc_tak":
            global odpornosc_suplementy
            odpornosc_suplementy = []
            global odpornosc
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == odpornosc:
                        polecenie = str(suplement)
                        odpornosc_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            odpornosc_suplementy = None
        if serce_ankieta == "serce_tak":
            global serce_suplementy
            serce_suplementy = []
            global serce
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == serce:
                        polecenie = str(suplement)
                        serce_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            serce_suplementy = None
        if stawy_ankieta == "stawy_tak":
            global stawy_suplementy
            stawy_suplementy = []
            global stawy
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == stawy:
                        polecenie = str(suplement)
                        stawy_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            stawy_suplementy = None
        if trawienie_ankieta == "trawienie_tak":
            global trawienie_suplementy
            trawienie_suplementy = []
            global trawienie
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == trawienie:
                        polecenie = str(suplement)
                        trawienie_suplementy.append(polecenie[21:].replace("_", " "))
        else:
            trawienie_suplementy = None
        return redirect('wyniki')
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'ankieta.html', dane)


def wyniki(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    if request.method == "POST":
        polecane_koszyk = request.POST.get('koszyk_polecane')
        if polecane_koszyk == "sfd":
            cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
            supplement = Supplement.objects.get(id=36)
            ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegan_suplementy:
                supplement = Supplement.objects.get(id=25)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=11)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=36)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=34)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegetarian_suplementy:
                supplement = Supplement.objects.get(id=18)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=21)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=32)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=11)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=36)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=34)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if koncentracja_suplementy:
                supplement = Supplement.objects.get(id=40)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if sen_suplementy:
                supplement = Supplement.objects.get(id=16)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pamiec_suplementy:
                supplement = Supplement.objects.get(id=18)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=21)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=49)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if stres_suplementy:
                supplement = Supplement.objects.get(id=40)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=46)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if odpornosc_suplementy:
                supplement = Supplement.objects.get(id=46)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=1)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if serce_suplementy:
                supplement = Supplement.objects.get(id=46)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=21)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if trawienie_suplementy:
                supplement = Supplement.objects.get(id=58)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            return redirect('koszyk')
        elif polecane_koszyk == "allnutrition":
            cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
            supplement = Supplement.objects.get(id=37)
            ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegan_suplementy:
                supplement = Supplement.objects.get(id=37)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegetarian_suplementy:
                supplement = Supplement.objects.get(id=28)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=22)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=31)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=37)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if sen_suplementy:
                supplement = Supplement.objects.get(id=43)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pamiec_suplementy:
                supplement = Supplement.objects.get(id=28)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=22)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=50)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pobudzenie_suplementy:
                supplement = Supplement.objects.get(id=53)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wzrok_suplementy:
                supplement = Supplement.objects.get(id=47)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if odpornosc_suplementy:
                supplement = Supplement.objects.get(id=13)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if serce_suplementy:
                supplement = Supplement.objects.get(id=22)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if stawy_suplementy:
                supplement = Supplement.objects.get(id=56)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if trawienie_suplementy:
                supplement = Supplement.objects.get(id=59)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            return redirect('koszyk')
        elif polecane_koszyk == "kfd":
            cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
            supplement = Supplement.objects.get(id=2)
            ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegan_suplementy:
                supplement = Supplement.objects.get(id=27)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=39)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=2)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegetarian_suplementy:
                supplement = Supplement.objects.get(id=30)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=24)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=39)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if koncentracja_suplementy:
                supplement = Supplement.objects.get(id=42)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if sen_suplementy:
                supplement = Supplement.objects.get(id=45)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pamiec_suplementy:
                supplement = Supplement.objects.get(id=30)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=24)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=52)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if stres_suplementy:
                supplement = Supplement.objects.get(id=42)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pobudzenie_suplementy:
                supplement = Supplement.objects.get(id=55)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if odpornosc_suplementy:
                supplement = Supplement.objects.get(id=19)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if serce_suplementy:
                supplement = Supplement.objects.get(id=24)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            return redirect('koszyk')
        elif polecane_koszyk == "olimp":
            cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
            if wegan_suplementy:
                supplement = Supplement.objects.get(id=26)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=38)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=35)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wegetarian_suplementy:
                supplement = Supplement.objects.get(id=29)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=23)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=33)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=12)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=38)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=35)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if koncentracja_suplementy:
                supplement = Supplement.objects.get(id=41)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if sen_suplementy:
                supplement = Supplement.objects.get(id=44)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pamiec_suplementy:
                supplement = Supplement.objects.get(id=29)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=23)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
                supplement = Supplement.objects.get(id=51)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if stres_suplementy:
                supplement = Supplement.objects.get(id=41)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if pobudzenie_suplementy:
                supplement = Supplement.objects.get(id=54)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if wzrok_suplementy:
                supplement = Supplement.objects.get(id=48)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if odpornosc_suplementy:
                supplement = Supplement.objects.get(id=20)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if serce_suplementy:
                supplement = Supplement.objects.get(id=23)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            if stawy_suplementy:
                supplement = Supplement.objects.get(id=57)
                ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement, ilosc=1)
            return redirect('koszyk')
        elif polecane_koszyk == "nie":
            return redirect('index')
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo, 'wegetarian': wegetarian_suplementy,
            'wegan': wegan_suplementy, 'koncentracja': koncentracja_suplementy, 'sen': sen_suplementy,
            'pamiec': pamiec_suplementy, 'stres': stres_suplementy, 'pobudzenie': pobudzenie_suplementy,
            'wzrok': wzrok_suplementy, 'odpornosc': odpornosc_suplementy, 'serce': serce_suplementy,
            'stawy': stawy_suplementy, 'trawienie': trawienie_suplementy}
    return render(request, 'wyniki.html', dane)



def kategoria(request, id):
    kategoria_adres = Kategoria.objects.get(pk=id)
    kategoria_suplement = Supplement.objects.filter(kategoria=kategoria_adres)
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategoria_adres': kategoria_adres,
            'kategoria_suplement': kategoria_suplement,
            'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'kategoria_suplement.html', dane)


def producent(request, id):
    producent_adres = Producent.objects.get(pk=id)
    producent_suplementy = Supplement.objects.filter(producent=producent_adres)
    producenci = Producent.objects.all()
    kategorie = Kategoria.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    data = {'producent_adres': producent_adres,
            'producent_suplementy': producent_suplementy,
            'producenci': producenci, 'kategorie': kategorie, 'logo': logo}
    return render(request, 'producenci.html', data)


def suplement(request, id):
    suplement_adres = Supplement.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'suplement_adres': suplement_adres, 'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    if request.method == 'POST':
        global quantity
        quantity = request.POST.get('ilosc')
    return render(request, 'suplement.html', dane)


@login_required(login_url='/login/')
def profil(request):
    nazwa = User.username
    imie = User.first_name
    nazwisko = User.last_name
    mail = User.email
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'nazwa': nazwa, 'imie': imie, 'nazwisko': nazwisko, 'mail': mail,
            'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'profil.html', dane)


def strona_rejestracji(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto zostało założone, witamy ' + user)
                return redirect('login')
    context = {'form': form}
    return render(request, 'rejestracja.html', context)


def strona_logowania(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Nazwa użytkownika bądź hasło zostało źle wpisane')

        context = {}
        return render(request, 'login.html', context)


def wylogowanie(request):
    logout(request)
    return redirect('login')


class EdycjaProfilu(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edycja_profilu.html'
    success_url = reverse_lazy('profil')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('zmienione_haslo')


@login_required(login_url='/login/')
def zmienione_haslo(request):
    return render(request, 'zmienione_haslo.html', {})


@login_required(login_url='/login/')
def koszyk(request):
    cart = None
    cartitems = []
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")

    if request.user.is_authenticated:
        cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
        cartitems = cart.cartitems.all()
    context = {"cart": cart, "items": cartitems, 'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, "koszyk.html", context)


@login_required(login_url='/login/')
def dodanie_do_koszyka(request):
    data = json.loads(request.body)
    supplement_id = data["id"]
    supplement = Supplement.objects.get(id=supplement_id)

    if request.user.is_authenticated:
        cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
        suplement(request, id=supplement_id)
        cartitem, created = ElementKoszyka.objects.get_or_create(koszyk=cart, produkt=supplement)
        global quantity
        ilosc = quantity
        if not cartitem.ilosc:
            if ilosc:
                cartitem.ilosc += int(ilosc)
                cartitem.save()
            else:
                cartitem.ilosc += 1
                cartitem.save()
    return JsonResponse("Dodawanie do koszyka", safe=False)


@login_required(login_url='/login/')
def aktualizacja_koszyka_plus(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    cartitem.ilosc += 1
    cartitem.save()
    return JsonResponse("Edycja koszyka", safe=False)


@login_required(login_url='/login/')
def aktualizacja_koszyka_minus(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    if cartitem.ilosc > 1:
        cartitem.ilosc -= 1
        cartitem.save()
    return JsonResponse("Edycja koszyka", safe=False)


@login_required(login_url='/login/')
def usuwanie_elementu(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    cartitem.delete()
    if not cart.cartitems:
        cart.delete()
    return JsonResponse("Edycja koszyka", safe=False)


@login_required(login_url='/login/')
def pusty_koszyk(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cart.delete()
    return JsonResponse("Pusty koszyk", safe=False)


def brak_koszyka(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'brak_koszyka.html', dane)


def szuakj(request):
    q = request.GET['q']
    suplementy = Supplement.objects.filter(nazwa__icontains=q)
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'suplementy': suplementy, 'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'szukaj.html', dane)


@login_required(login_url='/login/')
def numer_telefonu(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'numer_telefonu.html', dane)


@login_required(login_url='/login/')
def zamowienie(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitems = cart.cartitems.all()
    if not cartitems:
        return render(request, 'brak_koszyka.html')
    if request.method == "POST":
        global name
        name = request.POST.get('nazwa')
        global surname
        surname = request.POST.get('nazwisko')
        global tel_number
        tel_number = request.POST.get('numer_tel')
        global city
        city = request.POST.get('miasto')
        global post
        post = request.POST.get('kod_pocztowy')
        global delivery
        delivery = request.POST.get('dostawa')
        global payment
        payment = request.POST.get('rozliczenie')
        global discount_code
        code = request.POST.get('kod')
        cart = Koszyk.objects.get(klient=request.user, zamowione=False)
        kwota = cart.kompletna_kwota
        if name and surname and tel_number and city and post and delivery and payment:
            if 6 < len(tel_number) < 13:
                if delivery == "dostawa_kurier":
                    global delivery_cost
                    delivery_cost = 15
                discount_codes = KodyRabatowe.objects.all()
                for code_name in discount_codes:
                    if code_name.nazwa == code:
                        kwota *= code_name.procent
                order, created = Zamowienie.objects.get_or_create(koszyk=cart)
                order.imie = name
                order.nazwisko = surname
                order.numer_telefonu = tel_number
                order.miasto = city
                order.kod_pocztowy = post
                order.zamowione = True
                order.kwota = kwota + delivery_cost
                order.kwota = round(order.kwota, 2)
                order.save()
                message = ""
                for element in cartitems:
                    product = "Produkt: " + element.produkt.nazwa + "\n"
                    product = product + ('Ilość: ' + str(element.ilosc) + "\n")
                    product = product + ("Cena za sztukę: " + element.produkt.cena + "\n \n")
                    message = message + product
                global order_id
                order_id = order.id
                if payment == "pobranie":
                    cart.zamowione = True
                    cart.save()
                    send_mail(
                        'Zamówienie',
                        "Dziękujemy za złożenie zamówienia! \n"
                        "Twoje zamówienie o numerze " + str(order.id) + " jest w trakcie realizacji.\n \n"
                        + str(message) + "\n"
                                         "Całkowity koszt zamówienia: " + str(order.kwota) + " zł. \n"
                                                                                             "Pozdrawiamy, SKLEP Z SUPLEMENTAMI!",
                        'settings.EMAIL_HOST_USER',
                        [request.user.email],
                        fail_silently=False)
                    return redirect('podsumowanie')
                else:
                    return redirect('rozliczenie')
            else:
                return redirect("numer_telefonu")
    return render(request, 'zamowienie.html', dane)


@login_required(login_url='/login/')
def rozliczenie(request):
    global order_id
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    try:
        order = Zamowienie.objects.get(id=order_id)
        cart = Koszyk.objects.get(klient=request.user, zamowione=False)
        cartitems = cart.cartitems.all()
        if not cartitems:
            return render(request, 'brak_koszyka.html')
    except:
        return render(request, 'brak_koszyka.html')
    context = {"order": order, 'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'rozliczenie.html', context)


@login_required(login_url='/login/')
def udane_rozliczenie(request):
    global order_id
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    try:
        order = Zamowienie.objects.get(id=order_id)
        cart = order.koszyk
        cartitems = cart.cartitems.all()
        if not cartitems:
            return render(request, 'brak_koszyka.html')
    except:
        return render(request, 'brak_koszyka.html')
    cart.zamowione = True
    cart.save()
    order.zamowione = True
    order.save()
    total_cost = order.kwota
    global delivery_cost
    products_cost = order.kwota - delivery_cost
    delivery_cost = 0
    context = {"order": order, "cart": cart, "items": cartitems, "total_cost": total_cost, "cost": products_cost,
               'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    message = ""
    for element in cartitems:
        product = "Produkt: " + element.produkt.nazwa + "\n"
        product = product + ('Ilość: ' + str(element.ilosc) + "\n")
        product = product + ("Cena za sztukę: " + element.produkt.cena + "\n \n")
        message = message + product
    send_mail(
        'Zamówienie',
        "Dziękujemy za złożenie i opłacenie zamówienia! \n"
        "Twoje zamówienie o numerze " + str(order.id) + " jest w trakcie realizacji.\n \n"
        + str(message) + "\n"
                         "Całkowity koszt zamówienia: " + str(
            order.kwota) + " zł. \n"
                           "Pozdrawiamy, SKLEP Z SUPLEMENTAMI!",
        'settings.EMAIL_HOST_USER',
        [request.user.email],
        fail_silently=False)
    return render(request, 'udane_rozliczenie.html', context)


@login_required(login_url='/login/')
def podsumowanie(request):
    global order_id
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    try:
        order = Zamowienie.objects.get(id=order_id)
        cart = order.koszyk
        cartitems = cart.cartitems.all()
        if not cartitems:
            return render(request, 'brak_koszyka.html')
    except:
        return render(request, 'brak_koszyka.html')
    total_cost = order.kwota
    global delivery_cost
    products_cost = order.kwota - delivery_cost
    delivery_cost = 0
    context = {"order": order, "cart": cart, "items": cartitems, "total_cost": total_cost, "cost": products_cost,
               'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'podsumowanie.html', context)


@login_required(login_url='/login/')
def historia_zamowien(request):
    orders = Zamowienie.objects.all()
    user_orders = []
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    for order in orders:
        if order.koszyk.klient == request.user:
            user_orders.append(order)
    context = {"orders": user_orders, 'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'historia_zamowien.html', context)


@login_required(login_url='/login/')
def historia_zamowien_id(request, id):
    order = Zamowienie.objects.get(pk=id)
    cart = order.koszyk
    cartitems = cart.cartitems.all()
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    context = {"order": order, "cart": cart, "items": cartitems, 'kategorie': kategorie,
               'producenci': producenci, 'logo': logo}
    return render(request, 'historia_zamowien_id.html', context)
