from django.urls import path
from .views import GetEmpleadoView, CreateEmployeView, ModifierEmployeView, DeleteEmployeView, RetrieveAreas

urlpatterns = [
    path('listar-empleados/', GetEmpleadoView.as_view(), name='lista_empleados'),
    path('crear-empleados/', CreateEmployeView.as_view(), name='crear_empleados'),
    path('modificar-empleados/<int:id>', ModifierEmployeView.as_view(),name='modificar_empleados'),
    path('borrar-empleados/<int:id>', DeleteEmployeView.as_view(), name='borrar_empleados'),
    #Area
    path('areas/', RetrieveAreas.as_view())

]
