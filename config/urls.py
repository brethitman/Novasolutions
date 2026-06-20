from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

# Importa desde config.views porque está dentro de la carpeta config
from config.views import (
    home,
    about,
    services,
    contact
)

# 1. Rutas del sistema global sin prefijo de idioma
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  
]

# 2. Rutas dinámicas con soporte multiidioma protegidas por URLs secretas
# Nota: La raíz ('') la dejamos libre para que cargue tu Home.
urlpatterns += i18n_patterns(
    path('', home, name='home'),
    
    # Añadimos un token secreto antes o después del nombre de la ruta
    path('about-secure-9x2v1/', about, name='about'),
    path('services-priv-4m8z0/', services, name='services'),
    path('contact-auth-7w1p3/', contact, name='contact'),
)