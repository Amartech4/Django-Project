from django.shortcuts import render
from .models import product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    item = product.objects.all()
    return render(request, 'product.html', {'products': item})