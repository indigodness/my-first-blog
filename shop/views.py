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

def bakery(request):
    posts = Product.objects.all()
    return render(request, 'shop/bakery.html', {'posts': posts})

def cereal(request):
    posts = Product.objects.all()
    return render(request, 'shop/cereal.html', {'posts': posts})

def diary(request):
    posts = Product.objects.all()
    return render(request, 'shop/diary.html', {'posts': posts})

def drinks(request):
    posts = Product.objects.all()
    return render(request, 'shop/drinks.html', {'posts': posts})

def frozen(request):
    posts = Product.objects.all()
    return render(request, 'shop/frozen.html', {'posts': posts})

def meat(request):
    posts = Product.objects.all()
    return render(request, 'shop/meat.html', {'posts': posts})

def snack(request):
    posts = Product.objects.all()
    return render(request, 'shop/snack.html', {'posts': posts})

def vegan(request):
    posts = Product.objects.all()
    return render(request, 'shop/vegan.html', {'posts': posts})
