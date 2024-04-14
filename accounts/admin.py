from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'age', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),  # Note the comma after 'age' to make it a tuple
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),  # Similarly here
    )

admin.site.register(CustomUser, CustomUserAdmin)