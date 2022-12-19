from django.contrib import admin
from .models import WishListItems
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
@admin.register(WishListItems)
class WislistitemLinestack(admin.ModelAdmin):
    model = WishListItems
    #list_display = '__all__'