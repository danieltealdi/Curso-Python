"""webDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    #path('', views.index, name='index'),
    
    path('users/login', views.login, name='login'),    
    path('index', views.index, name='index'),
    path('accounts/profile/', views.index, name='index'),
    path('salir', views.salir, name='salir'),
    path('users/registro', views.registro, name='registro'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
SOCIAL_AUTH_URL_NAMESPACE = 'social'
