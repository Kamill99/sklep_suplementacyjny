from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from Main.serializers import UserSerializer
from .models import Supplement, Ocena
from .serializers import SupplementSerializer, OcenySerializer
from django.http.response import HttpResponseNotAllowed


class SupplementSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplementViewSet(viewsets.ModelViewSet):
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SupplementSetPagination

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            suplement = Supplement.objects.create(nazwa=request.data['nazwa'],
                                                  opis=request.data['opis'],
                                                  dostepnosc=request.data['dostepnosc'],
                                                  cena=request.data['cena'],
                                                  rodzaj_suplementu=request.data['rodzaj_suplementu'],
                                                  pojemnosc_suplementu=request.data['pojemnosc_suplementu'],)
            serializer = SupplementSerializer(suplement, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        suplement = self.get_object()
        suplement.nazwa = request.data['nazwa']
        suplement.opis = request.data['opis']
        suplement.dostepnosc = request.data['dostepnosc']
        suplement.cena = request.data['cena']
        suplement.rodzaj_suplementu = request.data['rodzaj_suplementu']
        suplement.pojemnosc_suplementu = request.data['pojemnosc_suplementu']
        suplement.save()

        serializer = SupplementSerializer(suplement, many=False)
        return Response(serializer.data)


class OcenyViewSet(viewsets.ModelViewSet):
    queryset = Ocena.objects.all()
    serializer_class = OcenySerializer
    permission_classes = [permissions.IsAuthenticated]