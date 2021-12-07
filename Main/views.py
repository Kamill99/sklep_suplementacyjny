from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from Main.serializers import UserSerializer
from .models import Supplement
from .serializers import SupplementSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SupplementViewSet(viewsets.ModelViewSet):
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer
    permission_classes = [permissions.IsAuthenticated]
