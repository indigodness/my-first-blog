from django.shortcuts import render
from .models import Product

# Create your views here.

def post_list(request):
    posts = Product.objects.all()
    return render(request, 'shop/post_list.html', {'posts': posts})

