from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("teach/", views.teach, name="teach"),
    path("music/", views.music, name="music"),
    path("videos/", views.videos, name="videos")
]