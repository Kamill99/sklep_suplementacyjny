import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from rest_framework.reverse import reverse_lazy
from .forms import PasswordChangingForm
from .models import Supplement, Ocena, Kategoria, Koszyk, ElementKoszyka
from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


quantity = 0
change = 0


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'main.html', dane)


def kategoria(request, id):
    kategoria_adres = Kategoria.objects.get(pk=id)
    kategoria_suplement = Supplement.objects.filter(kategoria=kategoria_adres)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_adres': kategoria_adres,
            'kategoria_suplement': kategoria_suplement,
            'kategorie': kategorie}
    return render(request, 'kategoria_suplement.html', dane)


def suplement(request, id):
    suplement_adres = Supplement.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'suplement_adres': suplement_adres, 'kategorie': kategorie}
    if request.method == 'POST':
        global quantity
        quantity = request.POST.get('ilosc')
    return render(request, 'suplement.html', dane)


def profil(request):
    nazwa = User.username
    imie = User.first_name
    nazwisko = User.last_name
    mail = User.email
    dane = {'nazwa': nazwa, 'imie': imie, 'nazwisko': nazwisko, 'mail': mail}
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

    if request.user.is_authenticated:
        cart, created = Koszyk.objects.get_or_create(klient=request.user, zamowione=False)
        cartitems = cart.cartitems.all()
    context = {"cart": cart, "items": cartitems}
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


def szuakj(request):
    q = request.GET['q']
    suplementy = Supplement.objects.filter(nazwa__icontains=q)
    dane = {'suplementy': suplementy}
    return render(request, 'szukaj.html', dane)
