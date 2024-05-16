from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


# Create your views here.

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                              subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
            contact.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form': form})


def videos(request):
    return render(request, 'videos.html')


def home(request):
    return render(request, 'home.html')


def music(request):
    return render(request, 'music.html')


def teach(request):
    return render(request, 'teach.html')
