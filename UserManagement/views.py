from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')


def gigs(request):
    return render(request, 'gigs/gigs.html')


def home(request):
    return render(request, 'home/home.html')


def music(request):
    return render(request, 'music/music.html')


def teach(request):
    return render(request, 'teach/teach.html')


def login(request):
    return render(request, 'music/login.html')


def logout(request):
    return render(request, 'music/logout.html')


def signup(request):
    return render(request, 'music/signup.html')


def weddings(request):
    return render(request, 'weddings/weddings.html')