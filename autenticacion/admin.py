from django.contrib import admin
from .models import User,Role
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'nombre')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','rol')

admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)