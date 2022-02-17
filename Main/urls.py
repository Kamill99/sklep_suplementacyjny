from django.urls import include, path
from rest_framework import routers
from Main import views
from Main.views import index

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'supplement', views.SupplementViewSet)
# router.register(r'oceny', views.OcenyViewSet)

urlpatterns = [
    # path('', include(router.urls))
    path('', index)
]
