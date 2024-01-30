from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role
from rest_framework.permissions import BasePermission
from .serializers import SerializerUser
from rest_framework import status

# Create your views here.

class RegisterUserView(APIView):
    def post(Self,request):
        serializer= SerializerUser(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


    

