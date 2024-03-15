from django.contrib import admin
from .models import Empleado, Tarea
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'cargo')

class TareaAdmin(admin.ModelAdmin):
    list_display = ('concepto','descripcion','f_inicio','f_fin')

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Tarea,TareaAdmin)