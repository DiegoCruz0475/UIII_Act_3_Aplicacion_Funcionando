from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_joyeria, name='inicio_joyeria'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),
]