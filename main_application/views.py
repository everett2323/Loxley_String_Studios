from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm
from .models import Contact


# Create your views here.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_login(request):
    # TODO: Change name to better representation name.
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        contacts = Contact.objects.filter(name__icontains=search_query)
    else:
        contacts = Contact.objects.none()



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "admin_contacts.html")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


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
    return render(request, 'contact.html', {'form': form})


def videos(request):
    return render(request, 'videos.html')


def home(request):
    return render(request, 'home.html')


def music(request):
    return render(request, 'music.html')


def teach(request):
    return render(request, 'teach.html')
