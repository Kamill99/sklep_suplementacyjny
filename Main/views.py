from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from Main.serializers import UserSerializer
from .models import Supplement, Ocena, Kategoria
from .serializers import SupplementSerializer, OcenySerializer
from django.http.response import HttpResponseNotAllowed, HttpResponse
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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

# class SupplementSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 3


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = (TokenAuthentication,)
#
#
# class SupplementViewSet(viewsets.ModelViewSet):
#     queryset = Supplement.objects.all()
#     serializer_class = SupplementSerializer
#     permission_classes = [permissions.AllowAny]
#     # pagination_class = SupplementSetPagination
#
#     # def create(self, request, *args, **kwargs):
#     #     if request.user.is_staff:
#     #         suplement = Supplement.objects.create(nazwa=request.data['nazwa'],
#     #                                               opis=request.data['opis'],
#     #                                               dostepnosc=request.data['dostepnosc'],
#     #                                               cena=request.data['cena'],
#     #                                               rodzaj_suplementu=request.data['rodzaj_suplementu'],
#     #                                               pojemnosc_suplementu=request.data['pojemnosc_suplementu'],)
#     #         serializer = SupplementSerializer(suplement, many=False)
#     #         return Response(serializer.data)
#     #     else:
#     #         return HttpResponseNotAllowed('Not allowed')
#     #
#     # def update(self, request, *args, **kwargs):
#     #     suplement = self.get_object()
#     #     suplement.nazwa = request.data['nazwa']
#     #     suplement.opis = request.data['opis']
#     #     suplement.dostepnosc = request.data['dostepnosc']
#     #     suplement.cena = request.data['cena']
#     #     suplement.rodzaj_suplementu = request.data['rodzaj_suplementu']
#     #     suplement.pojemnosc_suplementu = request.data['pojemnosc_suplementu']
#     #     suplement.save()
#     #
#     #     serializer = SupplementSerializer(suplement, many=False)
#     #     return Response(serializer.data)
#
#
# class OcenyViewSet(viewsets.ModelViewSet):
#     queryset = Ocena.objects.all()
#     serializer_class = OcenySerializer
#     permission_classes = [permissions.IsAuthenticated]
