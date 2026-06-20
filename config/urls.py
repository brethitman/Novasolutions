from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from .views import (
    home,
    about,
    services,
    contact
)

# 1. Rutas del sistema global (Debe ir AQUÍ arriba y limpio)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # <--- Este procesa el formulario del botón
]

# 2. Rutas dinámicas de tu web con soporte multiidioma
urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('ab13564ouasdt/', about, name='about'),
    path('sas123454asd/', services, name='services'),
    path('trhr5431cd/', contact, name='contact'),
)