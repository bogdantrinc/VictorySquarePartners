from django.contrib import admin
from .models import Car, CarAdmin, User, UserAdmin

admin.site.register(Car, CarAdmin)
admin.site.register(User, UserAdmin)

# Register your models here.
