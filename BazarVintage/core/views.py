from django.shortcuts import render
from .models import Product

# Create your views here.

# def index(request):
#     return render(request, 'index.html', {
#         'banner_image': 'img/banner_home.jpg', 
#         'banner_text': 'Vintage & Deco',})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'banner_image': 'img/banner_home.jpg', 
        'banner_text': 'Vintage & Deco',
        'products': products})

# def products(request):
#     return render(request, 'products.html', {'banner_image': 'img/banner_products.jpg', 'banner_text': 'Nuestros productos'})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'banner_image': 'img/banner_products.jpg', 
        'banner_text': 'Nuestros productos',
        'products': products})

# def sales(request):
#     return render(request, 'sales.html', {'banner_image': 'img/banner_sale.jpeg', 'banner_text': ''})

def sales(request):
    products = Product.objects.filter(sale=True)
    return render(request, 'sales.html', {
        'banner_image': 'img/banner_sale.jpeg', 
        'banner_text': 'Ofertas',
        'products': products})

def about(request):
    return render(request, 'about.html', {'banner_image': 'img/banner_about.jpg', 'banner_text': 'Sobre nosotros'})

def contact(request):
    return render(request, 'contact.html', {'banner_image': 'img/banner_contact.jpg', 'banner_text': 'Contacto'})