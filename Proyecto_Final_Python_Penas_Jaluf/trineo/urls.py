from django.urls import path
from trineo.views import ListadoTrineos, CrearTrineos, EditarTrineos, EliminarTrineos, DetalleTrineos


urlpatterns = [
     path('trineos/', ListadoTrineos.as_view(), name='trineos'),
     path('trineos/crear', CrearTrineos.as_view(), name='crear_trineo'),
     path('trineos/<int:pk>', DetalleTrineos.as_view(), name='detalle_trineo'),
     path('trineos/<int:pk>/editar', EditarTrineos.as_view(), name='editar_trineo'),
     path('trineos/<int:pk>/eliminar', EliminarTrineos.as_view() ,name='eliminar_trineo'),
]
