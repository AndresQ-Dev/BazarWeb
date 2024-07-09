from django.db import models

# Create your models here.
class Product(models.Model):
    idProduct = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Nombre')
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=False, default=0.00, null=False, verbose_name='Precio')
    stock = models.IntegerField(blank=False, null=False, verbose_name='Stock')
    description = models.TextField(max_length=150, blank=False, null=False, verbose_name='Descripción')
    category_choices = [
        ('Madera', 'Madera'),
        ('Bazar', 'Bazar'),
        ('Deco', 'Deco'),
    ]
    category = models.CharField(max_length=100, choices=category_choices, blank=False, null=False, verbose_name='Categoría')
    image = models.ImageField(upload_to='products/', blank=True, null=True, default='products/default_image.jpg', verbose_name='Imagen')
    sale = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.name