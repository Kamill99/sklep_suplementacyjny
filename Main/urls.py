from django.urls import include, path
from rest_framework import routers
from Main import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'supplement', views.SupplementViewSet)
router.register(r'oceny', views.OcenyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
