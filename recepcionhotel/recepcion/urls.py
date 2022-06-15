from django.urls import path
from recepcion.views import *

urlpatterns = [
    path('', index, name="index"),
    path('carga_huesped/', agregarhuesped, name="cargar_huesped"),
    path('carga_pago/', agregarpagotarjeta, name="cargar_pago"),
    path('carga_habitacion/', agregarhabitacion, name="cargar_habitacion"),
    path('borrar_huesped/<identificador>', borrarhuesped, name="borrar_huesped"),
    path('borrar_pago/<identificador>', borrarpagotarjeta, name="borrar_pago"),
    path('borrar_habitacion/<identificador>', borrarhabitacion, name="borrar_habitacion"),
    path('actualizar_huesped/', actualizarhuesped, name="actualizar_huesped"),
    path('actualizar_huesped/<identificador>', actualizarhuesped, name="actualizar_huesped"),
    path('actualizar_pago/<identificador>', actualizarpagotarjeta, name="actualizar_pago"),
    path('actualizar_pago/', actualizarpagotarjeta, name="actualizar_pago"),
    path('actualizar_habitacion/', actualizarhabitacion, name="actualizar_habitacion"),
    path('actualizar_habitacion/<identificador>', actualizarhabitacion, name="actualizar_habitacion"),
    path('buscar_huesped/', buscarhuesped, name="buscar_huesped"),
    path('buscar_pago/', buscarpagotarjeta, name="buscar_pago"),
    path('buscar_habitacion/', buscarhabitacion, name="buscar_habitacion"),
    path('lista_pagos/', listapagos, name="lista_pagos"),
    path('lista_habitaciones/', listahabitaciones, name="lista_habitaciones"),

]





