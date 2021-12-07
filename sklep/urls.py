from django.contrib import admin

from django.urls import include, path
from Main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Main', include(urls)),
]
