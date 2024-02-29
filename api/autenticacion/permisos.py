from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.rol.rol == 'admin':
            return True
        

class IsAdult(BasePermission):
    def has_permission(self, request, view):
        if request.user.age > 20 and request.user.sex == 'masculino':
            return True