"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from example import views as vw
from bank import views as vw1
from quiztest import views as vw2
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", views.hello),
    path("manas/", views.manas),
    path("calculate/",views.calculate),
    path("insert/",vw.insert),
    path("delete/",vw.delete),
    path("find/",vw.find),
    path("update/",vw.update),
    path("edit/",vw.edit),
    path("registration/",vw1.registration),
    path("withdrawDeposit/",vw1.withdrawDeposit),
    path("test/",vw2.test),
    path("wheather/",views.wheather),
    path("", views.index),
    
]
