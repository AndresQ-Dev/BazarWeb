from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Q

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'sale', 'image_tag') #agrego columnas a mostrar 
    search_fields = ['name', 'description'] #campo por el cual realiza la búsqueda (recibe tupla)
    actions = ['to_sale', 'out_sale']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Modificar la busqueda para que sea case insensitive
        search_term_normalized = search_term.lower()  # Convierto a minúsculas
        queryset |= self.model.objects.filter(
            Q(name__icontains=search_term_normalized)
        )
        return queryset, use_distinct
    
    def image_tag(self, obj):# Para mostrar la imágen en vez del URL de la imágen...
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Image'
    
    # Implementación de "ACTIONS" para enviar masivamente productos a Sale.
    def to_sale(self, request, queryset):
        updated = queryset.update(sale=True)
        self.message_user(request, f'{updated} productos han sido enviados a SALE')
    to_sale.short_description = 'Marcar productos seleccionados para Sale'
    
    # "ACTIONS" para sacar masivamente productos de Sale.
    def out_sale(self, request, queryset):
        updated = queryset.update(sale=False)
        self.message_user(request, f'{updated} productos han sido retirados de SALE')
    out_sale.short_description = 'Marcar productos seleccionados para retirar de Sale'
    
admin.site.register(Product, ProductAdmin)