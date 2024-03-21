from django.shortcuts import render

# Create your views here.
def weddings(request):
    return render(request, 'weddings/weddings.html')