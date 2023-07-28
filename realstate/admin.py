from django.contrib import admin 
from .models import Category,Property,Blog

# Register your models here.
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Blog)