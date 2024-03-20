from django.contrib import admin
from .models import UserProfile, Item, Menu, Order


admin.site.register(UserProfile) 
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)

