import json

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

quantity = tel_number = order_id = delivery_cost = 0
name = surname = city = post = delivery = payment = discount_code = ""

onto = get_ontology("C:\\Users\\user\\Desktop\\suplementy\\suplementy.owl")
onto.load()
suplementy = []
ashwagandha = berberyna = cynk = kofeina = kolagen = luteina = magnez = melatonina = cbd = omega = rhodiola = \
    wapn = witamina_a = witamina_b = witamina_c = witamina_d = None
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

trawienie = "untitled-ontology-15.przeznaczenie.some(untitled-ontology-15.Trawienie)"


def index(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    popularne_suplementy = [Supplement.objects.get(id=1), Supplement.objects.get(id=37), Supplement.objects.get(id=33)]
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo,
            'popularne_suplementy': popularne_suplementy}
    # berberyna = "untitled-ontology-15.Berberyna"
    # suplementy = "untitled-ontology-15.Suplement"
    # global klasa_berberyna
    # global klasa_suplement
    # for p in onto.classes():
    #     if str(p) == berberyna:
    # print("Jest")
    # klasa_berberyna = p
    # if str(p) == suplementy:
    # print("Jest suplement")
    # klasa_suplement = p
    # print(issubclass(klasa_berberyna, klasa_suplement)) #działa
    # print(list(klasa_suplement.subclasses())) # wypisuje obiekty pod daną klasą
    # print(klasa_berberyna.is_a) # wypisuje połączenia tego obiektu
    return render(request, 'main.html', dane)


def ankieta(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    if request.method == "POST":
        trawienie_polecenia = request.POST.get('trawienie')
        if trawienie_polecenia == "trawienie_tak":
            global trawienie
            for suplement in suplementy:
                for wskazanie in suplement.is_a:
                    if str(wskazanie) == trawienie:
                        polecenie = str(suplement)
                        print(polecenie[21:])
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'ankieta.html', dane)


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


def zmienione_haslo(request):
    return render(request, 'zmienione_haslo.html', {})


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
                # messages.success(request, 'Produkt dodany do koszyka')
            else:
                cartitem.ilosc += 1
                cartitem.save()
                # messages.success(request, 'Produkt dodany do koszyka')
        else:
            pass
            # messages.warning(request, 'Produkt jest już w koszyku')
    return JsonResponse("Dodawanie do koszyka", safe=False)


def aktualizacja_koszyka_plus(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    cartitem.ilosc += 1
    cartitem.save()
    return JsonResponse("Edycja koszyka", safe=False)


def aktualizacja_koszyka_minus(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    if cartitem.ilosc > 1:
        cartitem.ilosc -= 1
        cartitem.save()
    return JsonResponse("Edycja koszyka", safe=False)


def usuwanie_elementu(request):
    data = json.loads(request.body)
    cart = Koszyk.objects.get(klient=request.user, zamowione=False)
    cartitem = ElementKoszyka.objects.get(id=data["id"], koszyk=cart)
    cartitem.delete()
    if not cart.cartitems:
        cart.delete()
    return JsonResponse("Edycja koszyka", safe=False)


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


def numer_telefonu(request):
    kategorie = Kategoria.objects.all()
    producenci = Producent.objects.all()
    logo = Foto.objects.get(nazwa="Logo")
    dane = {'kategorie': kategorie, 'producenci': producenci, 'logo': logo}
    return render(request, 'numer_telefonu.html', dane)


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
