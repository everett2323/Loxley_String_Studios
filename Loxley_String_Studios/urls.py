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
from django.urls import path,re_path
from django.shortcuts import redirect

from home.views import home
from music.views import music
from teach.views import teach
from gigs.views import gigs
from weddings.views import weddings
from contact.views import contact
from about.views import about
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',lambda request: redirect('home/', permanent=False)),
    path('home/', home, name='home/'),
    path("music/", music, name='music/'),
    path("teach/", teach, name='teach/'),
    path("gigs/",gigs, name='gigs/'),
    path("weddings/", weddings, name='weddings/'),
    path("contact/", contact, name='contact/'),
    path("about/", about, name='about/')
]
