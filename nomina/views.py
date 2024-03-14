from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmpleadoSerializer,TareaSerializer, AreaSerializer, MaquinaSerializer
from .models import Empleado, Tarea, Area, Maquina
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from autenticacion.permisos import IsAdmin


class GetEmpleadoView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        lista_empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(lista_empleados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateEmployeView(APIView):
    def post(self, request):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ModifierEmployeView(APIView):
    def put(self,request,id):
        empleado= get_object_or_404(Empleado, pk=id)
        serializer = EmpleadoSerializer(empleado,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DeleteEmployeView(APIView):
    def delete(self,request,id):
        empleado= get_object_or_404(Empleado, pk=id)
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CreateTareaView(APIView):
    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveAreas(APIView):
    def get(self, request):
        lista_areas= Area.objects.all()
        serializer= AreaSerializer(data=lista_areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        