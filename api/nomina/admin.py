from django.contrib import admin
from .models import Empleado, Tarea, Maquina, Area

class EmpleadoInline(admin.TabularInline):
    model = Empleado
    extra = 1  # Esto controla cuántos formularios en línea se muestran de forma predeterminada

class AreaAdmin(admin.ModelAdmin):
    list_display=('nombre','capacidad')
    inlines = [EmpleadoInline]  # Agregamos la clase EmpleadoInline al administrador de Área

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'cargo')

class TareaAdmin(admin.ModelAdmin):
    list_display = ('concepto','descripcion','f_inicio','f_fin')

class MaquinaAdmin(admin.ModelAdmin):
    list_display=('marca','modelo')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Area, AreaAdmin)
