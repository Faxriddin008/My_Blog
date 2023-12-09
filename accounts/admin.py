from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
# from django.contrib import admin
# from .models import Trade, TradeInstance, Unit
#
#
#
# # Define the admin class
# @admin.register(Trade)
# class TradeAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     pass
