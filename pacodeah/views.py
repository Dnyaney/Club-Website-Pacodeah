from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'loader.html')

def landing_page(request): 
    return render(request, 'landing.html')