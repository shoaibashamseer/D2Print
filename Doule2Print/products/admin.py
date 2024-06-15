from django.contrib import admin
from .models import Product, Variety

'''class VarietyInline(admin.TabularInline):
    model = Product.varieties.through
    extra = 1
'''
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'retail_price')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','image')
    search_fields = ('name',)
    #inlines = [VarietyInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Variety, VarietyAdmin)
#admin.site.register(Customer)
#admin.site.register(Order)