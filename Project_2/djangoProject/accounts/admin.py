from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from accounts.forms import RegisterUser, EditUser

class UserAdmin(UserAdmin):
    add_form = RegisterUser
    form = EditUser
    model = User
    list_display = ('email', 'first_name','last_name', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('email', 'first_name','last_name', 'date_joined', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'address', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'address', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'first_name','last_name', 'address',)
    ordering = ('email', 'first_name','last_name', 'address', 'date_joined')


admin.site.register(User, UserAdmin)
