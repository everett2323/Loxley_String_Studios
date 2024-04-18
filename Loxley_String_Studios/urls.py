"""
URL configuration for Loxley_String_Studios project.

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

from UserManagement.views import home, music, teach, videos, weddings, contact, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("home/", home, name='home'),
    path("music/", music, name='music'),
    path("teach/", teach, name='teach'),
    path("videos/",videos, name='gigs'),
    path("weddings/", weddings, name='weddings'),
    path("contact/", contact, name='contact'),
    path("about/", about, name='about')
]
