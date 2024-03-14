from rest_framework import serializers
from .models import Empleado, Tarea, Area, Maquina


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    def to_representation(self, lista_empleados):
        #Instanciamos la variable representation en un objeto compatible con los datos de lo empleados.
        representation = super().to_representation(lista_empleados)
        #Tomo las tareas de los empleados 
        tareas_empleado = Tarea.objects.filter(empleado=lista_empleados)
        #Invocas a la clase serializer de las tareas para parsear a un objeto serializable
        tareas_serializer = TareaSerializer(tareas_empleado, many=True)
        #Se añade un atributo de nombre tareas y le asigno la lista de tareas que tomé en la linea anterior
        representation['tareas'] = tareas_serializer.data
        return representation

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'