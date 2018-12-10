"""jobportal_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from jp import views
from jp.views import UserUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('home/',views.showHome),
    path('openUserPage/',views.openUserPage),
    path('openNewRegister/',views.openNewRegister),
    path('getCityFromState/', views.getCityFromState),

    path('openAbout/',views.openAbout),
    path('showUserHome/',views.showUserHome),

    path('update_user<str:pk>/',UserUpdate.as_view)
  #   path('userRegister/', views.userRegister),
  #   path('loginUser/',views.loginUser),
  #   path('openUserHome/', views.openUserHome)
]
