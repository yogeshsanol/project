from django.contrib import admin
from app.models.category import Category
from app.models.product import Product

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
