from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser, Tag


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_filter  = ['is_active', 'is_staff', 'is_superuser']
    list_display = ['email', 'name', 'is_staff', 'is_superuser']

class CustomUserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model."""

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser')
    list_filter  = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tag)
