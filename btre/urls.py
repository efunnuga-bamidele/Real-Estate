
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('pages.url')),
    path('admin/', admin.site.urls),
]
