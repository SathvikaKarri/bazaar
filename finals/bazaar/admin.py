from django.contrib import admin
from .models import item, cart, CartItem

# Register your models here.
admin.site.register(item)
admin.site.register(cart)
admin.site.register(CartItem)