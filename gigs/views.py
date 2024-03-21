from django.shortcuts import render

# Create your views here.
def gigs(request):
    return render(request, 'gigs/gigs.html')