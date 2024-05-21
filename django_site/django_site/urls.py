"""
URL configuration for django_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from python_PRO.django_site.members_app.views import input_page, output_page
from python_PRO.django_site.courses_app.views import is_authenticated


urlpatterns = [
    path("admin/", admin.site.urls),
    path("input/", input_page),
    path("show/", output_page),
    path("is-authenticated/", is_authenticated),
]
