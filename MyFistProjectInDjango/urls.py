"""
URL configuration for MyFistProjectInDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),


    path('',views.Hola, name = "index"),
    path("saludar",views.Saludar, name = "saludar"),
    path("calcular",views.calcular, name = "calcular"),
    path("espar/<int:numero>",views.espar, name = "espar"),
    path("saludar/<str:nombre>",views.Saludar2, name = "saludar2"),
    

    path('hello', include("hello.urls")),
    path('clientes', include("clientes.urls"))
]
