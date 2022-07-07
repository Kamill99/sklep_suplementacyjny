from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from rest_framework.reverse import reverse_lazy
# from django.contrib.auth.forms import PasswordChangingForm
from .forms import PasswordChangingForm
from Main.serializers import UserSerializer
from .models import Supplement, Ocena, Kategoria
from .serializers import SupplementSerializer, OcenySerializer
from django.http.response import HttpResponseNotAllowed, HttpResponse
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required


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
    return render(request, 'suplement.html', dane)


def profil(request):
    nazwa = User.username
    imie = User.first_name
    nazwisko = User.last_name
    mail = User.email
    dane = {'nazwa': nazwa, 'imie': imie, 'nazwisko': nazwisko, 'mail': mail}
    return render(request, 'profil.html', dane)


def stronaRejestracji(request):
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


def stronaLogowania(request):
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
