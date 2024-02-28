from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmpleadoSerializer
from .models import Empleado
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#from autenticacion.views import IsAdmin

class GetEmpleadoView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Empleado.objects.all()
        serializer = EmpleadoSerializer(queryset, many=True)
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
