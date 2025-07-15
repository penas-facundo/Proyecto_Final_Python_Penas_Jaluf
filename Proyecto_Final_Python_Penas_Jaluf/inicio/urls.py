from django.urls import path
from inicio.views import inicio, paletas, autos, crear_paleta, crear_auto, crear_moto, motos, eliminar_paleta, editar_paleta, detalle_paleta, eliminar_auto, editar_auto, detalle_auto, editar_moto, eliminar_moto, detalle_moto, about_me

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),
    path('autos/', autos, name='autos'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('motos/crear/', crear_moto, name='crear_moto'),
    path('motos/', motos, name='motos'),
    path('paletas/<int:paleta_id>/eliminar/', eliminar_paleta, name='eliminar_paleta'),
    path('paletas/<int:paleta_id>/editar/', editar_paleta, name='editar_paleta'),
    path('paletas/<int:paleta_id>/', detalle_paleta, name='detalle_paleta'),
    path('autos/<int:auto_id>/eliminar/', eliminar_auto, name='eliminar_auto'),
    path('autos/<int:auto_id>/editar/', editar_auto, name='editar_auto'),
    path('autos/<int:auto_id>/', detalle_auto, name='detalle_auto'),
    path('motos/<int:moto_id>/eliminar/', eliminar_moto, name='eliminar_moto'),
    path('motos/<int:moto_id>/editar/', editar_moto, name='editar_moto'),
    path('motos/<int:moto_id>/', detalle_moto, name='detalle_moto'),
    path('about_me/', about_me, name='about_me'),
    
    
]
