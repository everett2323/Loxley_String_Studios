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
from home import views as homeviews
from music import views as musicviews
from teach import views as teachviews
from gigs import views as gigviews
from weddings import views as weddingviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeviews.home, name="home"),
    path("music", musicviews.music),
    path("teach", teachviews.teach),
    path("gigs", gigviews.gigs),
    path("weddings", weddingviews.weddings),
]
