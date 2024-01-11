from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmpleadoSerializer
from .models import Empleado

class GetEmpleadoView(APIView):
    def get(self, request):
        queryset= Empleado.objects.all()
        serializer= EmpleadoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



