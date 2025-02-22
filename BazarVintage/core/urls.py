from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
