from django.urls import path
from .views import GetEmpleadoView

urlpatterns = [
    path('listar-empleados/', GetEmpleadoView.as_view(), name='lista_empleados'),
]