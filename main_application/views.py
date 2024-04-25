from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def videos(request):
    return render(request, 'videos.html')


def home(request):
    return render(request, 'home.html')


def music(request):
    return render(request, 'music.html')


def teach(request):
    return render(request, 'teach.html')

