from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def videos(request):
    return render(request, 'gigs.html')


def home(request):
    return render(request, 'home.html')


def music(request):
    return render(request, 'music.html')


def teach(request):
    return render(request, 'teach.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def signup(request):
    return render(request, 'signup.html')


def weddings(request):
    return render(request, 'weddings.html')
