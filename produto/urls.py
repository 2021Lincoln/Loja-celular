"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import fproduto, fcadproduto, salvar, exibir, update, excluir, lista_capinha, lista_celular, lista_acessorios, flista_produtos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fproduto),
    path('fcadproduto/', fcadproduto, name='fcadproduto'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('exibir/<int:id>', exibir, name='exibir'),
    path('update/<int:id>', update, name='update'),
    path('lista_celular/', lista_celular, name='lista_celular'),
    path('lista_capinha/', lista_capinha, name='lista_capinha'),
    path('lista_acessorios/', lista_acessorios, name='lista_acessorios'),
    path('flista_produtos/', flista_produtos, name='flista_produtos'),

]
