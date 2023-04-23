""" THIS IS THE URL ROUTING SYSTEM """
"""dj_pypractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

# Tenemos que importar el archivo de settings.py para que funcionen las rutas de las imágenes
from django.conf.urls.static import static
from django.conf import settings

# importamos el HttpResponse con el fin de poder utilizar las functiones y conectar con las webs
# from django.http import HttpResponse

# #Ahora creamos las functions que nos van a conectar con las webpages
# def home(request):
#     return HttpResponse('Aqui colocamos la URL de nuestra web')

# def contact(request):
#     return HttpResponse('Contact')


# Una vez que tenemos las functions, tenemos que agregar después los paths (las rutas) a nuestras web
""" HERE IS WHERE WE PUT OUR PAGE URL. We let know Django what to do with our website """
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    # path('about/', contact),
    # como estamos utilizando otro archivo de urls tenemos que usar el include() para que django las
    # reconozca y se pueda navegar por las rutas sin problemas
    path('', include('accounts.urls')),
]

# Sumamos una urlpattern para poder utilizar las imágenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)