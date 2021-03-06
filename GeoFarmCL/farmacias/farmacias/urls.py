"""farmacias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
	url(r'^$', 'FarmaciasChile.views.index', name='index'),
    url(r'^admin/', admin.site.urls),
	url(r'^maps/$', 'FarmaciasChile.views.maps', name='maps'),
    url(r'^acercade/$', 'FarmaciasChile.views.acercade', name='acercade'),
    url(r'^farmacias/$', 'FarmaciasChile.views.farmacias', name='farmacias'),
    url(r'^autores/$', 'FarmaciasChile.views.autores', name='autores'),
    url(r'^conclusiones/$', 'FarmaciasChile.views.conclusiones', name='conclusiones'),
    url(r'^maps/resultados/$', 'FarmaciasChile.views.resultados', name='resultados'),
    url(r'^maps/filtrofarmacia/$', 'FarmaciasChile.views.filtrofarmacia', name='filtrofarmacia'),
    url(r'^maps/filtromedicamentos/$', 'FarmaciasChile.views.filtromedicamentos', name='filtromedicamentos'),
   #url(r'^ruta/$', 'FarmaciasChile.views.ruta', name="ruta"),
]
