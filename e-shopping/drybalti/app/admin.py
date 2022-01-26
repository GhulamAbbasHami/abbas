from django.contrib import admin
from .models import (User, Customer, Product,Cart, OrderPlaced)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','selling_price','dicounted_price','description','brand','catogory','product_image']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','use','product','quantity','oder_date','status']

