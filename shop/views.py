from django.shortcuts import render
from .models import Product

# Create your views here.

def main(request):
    posts = Product.objects.all()
    return render(request, 'shop/main.html', {'posts': posts})

def about(request):
    posts = Product.objects.all()
    return render(request, 'shop/about.html', {'posts': posts})

def stores(request):
    posts = Product.objects.all()
    return render(request, 'shop/stores.html', {'posts': posts})

