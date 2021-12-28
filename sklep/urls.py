from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from Main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Main/', include(urls)),
    path('api-token-auth/', obtain_auth_token),
]
