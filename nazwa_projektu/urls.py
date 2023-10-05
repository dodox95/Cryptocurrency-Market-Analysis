# nazwa_projektu / urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kryptoanaliza.urls')),  # Zmieniono 'kryptoanaliza/' na ''
]
