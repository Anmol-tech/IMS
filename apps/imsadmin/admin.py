from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.imsadmin.models import ImsUser


# Register your models here.
class ImsUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        (_('Personal Info'), {'fields': ('first_name', 'middle_name', 'last_name',)}),
        (_('Permissions'),
         {'fields': ('is_superuser',)}),
        (_('Important Dates'), {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
         ),
    )
    list_display = ('email', 'first_name', 'last_name', )
    list_filter = ('is_superuser', 'groups', )
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    ordering = ('email', 'created_at')
    raw_id_fields = ()


admin.site.register(ImsUser, ImsUserAdmin)
