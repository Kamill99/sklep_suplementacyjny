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
from django.shortcuts import render


def index(request):
    queryset = Supplement.objects.all()
    # kat_witaminy = Supplement.objects.filter(kategoria=1)
    # kat_zdrowie = Supplement.objects.filter(kategoria=2)
    # kat_mineraly = Supplement.objects.filter(kategoria=3)
    # kat_zdrowie_sen = Supplement.objects.filter(kategoria=4)
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'index.html', dane)


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
    dane = {'suplement_adres' : suplement_adres, 'kategorie': kategorie}
    return render(request, 'suplement.html', dane)

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
