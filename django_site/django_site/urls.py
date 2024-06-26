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

from members_app.views import input_info, output_info, index
from courses_app.views import is_authenticated


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("input/", input_info, name="input_information"),
    path("show/", output_info, name="output_information"),
    path("is-authenticated/", is_authenticated, name="is_authenticated"),
]
