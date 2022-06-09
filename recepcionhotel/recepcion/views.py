from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader 
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from recepcion.forms import *
from recepcion.models import Huesped, PagoTarjeta, Habitacion


def index(request):
    huespedes = Huesped.objects.all()
    template = loader.get_template('recepcion/index.html')
    context = {
        'huespedes': huespedes,
          
    }
    return HttpResponse(template.render(context, request))

def listapagos(request):
    tarjetas = PagoTarjeta.objects.all()
    template = loader.get_template('recepcion/lista_pagos.html')
    context = {
        'tarjetas' : tarjetas, 
    }
    return HttpResponse(template.render(context, request))

def listahabitaciones(request):
    habitaciones = Habitacion.objects.all()
    template = loader.get_template('recepcion/lista_habitaciones.html')
    context = {
        'habitaciones' : habitaciones, 
    }
    return HttpResponse(template.render(context, request))    


#FUNCIONESAGREGAR

def agregarhuesped(request):

    if request.method == "POST":
        form_huesped = AgregarhuespedForm(request.POST)
        if form_huesped.is_valid():

            nombre = form_huesped.cleaned_data['nombre']
            apellido = form_huesped.cleaned_data['apellido']
            documento = form_huesped.cleaned_data['documento']
            email = form_huesped.cleaned_data['email']
            formadepago = form_huesped.cleaned_data['formadepago']
            Huesped(nombre=nombre, apellido=apellido, documento=documento, email=email,formadepago=formadepago).save()
            return HttpResponseRedirect(reverse("index"))

    elif request.method == "GET":
        form_huesped = AgregarhuespedForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    return render(request, 'recepcion/carga_huesped.html', {'form_huesped': form_huesped})

def agregarpagotarjeta(request):
   
    if request.method == "POST":
        form_pago = AgregarPagoForm(request.POST)
        if form_pago.is_valid():
            nombrepropietario = form_pago.cleaned_data['nombrepropietario']
            numtarjeta = form_pago.cleaned_data['numtarjeta']
            codseguridad = form_pago.cleaned_data['codseguridad']
            cuotas = form_pago.cleaned_data['cuotas']
            valor = form_pago.cleaned_data['valor']
            PagoTarjeta(nombrepropietario = nombrepropietario, numtarjeta = numtarjeta, codseguridad = codseguridad, cuotas = cuotas, valor = valor).save()    
            return HttpResponseRedirect(reverse("lista_pagos"))

    elif request.method == "GET":
        form_pago = AgregarPagoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    return render(request, 'recepcion/carga_pago.html', {'form_pago': form_pago})


def agregarhabitacion(request):

    if request.method == "POST":
       form_habitacion = AgregarHabitacionForm(request.POST)
       if form_habitacion.is_valid():
          numhabitacion = form_habitacion.cleaned_data['numhabitacion']
          tipohabitacion = form_habitacion.cleaned_data['tipohabitacion']
          canthuespedes = form_habitacion.cleaned_data['canthuespedes']
          condicion = form_habitacion.cleaned_data['condicion'] 
          Habitacion(numhabitacion = numhabitacion, tipohabitacion = tipohabitacion, canthuespedes = canthuespedes, condicion = condicion).save()
          return HttpResponseRedirect(reverse("lista_habitaciones"))

    elif request.method == "GET":
        form_habitacion = AgregarHabitacionForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    return render(request, 'recepcion/carga_habitacion.html', {'form_habitacion': form_habitacion})


#FUNCIONBORRAR

def borrarhuesped(request, identificador):
    if request.method == "GET":
        huesped = Huesped.objects.filter(id=int(identificador)).first()
        if huesped:
            huesped.delete()
        return HttpResponseRedirect(reverse("index"))

def borrarpagotarjeta(request, identificador):
    if request.method == "GET":
       tarjeta = PagoTarjeta.objects.filter(id=int(identificador)).first()
       if tarjeta:
            tarjeta.delete()
    return HttpResponseRedirect(reverse("lista_pagos"))

def borrarhabitacion(request, identificador):
    if request.method == "GET":
        habitacion = Habitacion.objects.filter(id=int(identificador)).first()
        if habitacion:
            habitacion.delete()
    return HttpResponseRedirect(reverse("lista_habitaciones"))

#FUNCIONACTUALIZAR 

#HUESPED

def actualizarhuesped(request, identificador=''):
    
    if request.method == "GET":
        huesped = get_object_or_404(Huesped, pk=int(identificador))
        initial = {
            "id": huesped.id,
            "nombre": huesped.nombre,
            "apellido": huesped.apellido,
            "documento": huesped.documento,
            "email": huesped.email,
            "formadepago": huesped.formadepago,
        }

        form_actualizarhuesped = ActualizarhuespedForm(initial=initial)
        return render(request, 'recepcion/carga_huesped.html', {'form': form_actualizarhuesped, 'actualizar_huesped': True})

    elif request.method == "POST":
        form_actualizarhuesped = ActualizarhuespedForm(request.POST)
        if form_actualizarhuesped.is_valid():
            huesped = get_object_or_404(Huesped, pk=form_actualizarhuesped.cleaned_data['id'])
            huesped.nombre = form_actualizarhuesped.cleaned_data['nombre']
            huesped.apellido = form_actualizarhuesped.cleaned_data['apellido']
            huesped.documento = form_actualizarhuesped.cleaned_data['documento']
            huesped.email = form_actualizarhuesped.cleaned_data['email']
            huesped.formadepago = form_actualizarhuesped.cleaned_data['formadepago'] 
            huesped.save()
            return HttpResponseRedirect(reverse("index"))

#PAGO

def actualizarpagotarjeta(request, identificador=''):
    
    if request.method == "GET":
        tarjeta = get_object_or_404(PagoTarjeta, pk=int(identificador))
        initial = {
            "id": tarjeta.id,
            "nombrepropietario": tarjeta.nombrepropietario,
            "numtarjeta": tarjeta.numtarjeta,
            "codseguridad": tarjeta.codseguridad,
            "cuotas": tarjeta.cuotas,
            "valor": tarjeta.valor,
        }

        form_actualizarpago = ActualizarTarjetaForm(initial=initial)
        return render(request, 'recepcion/carga_pago.html', {'form': form_actualizarpago, 'actualizar_pago': True})

    elif request.method == "POST":
        form_actualizarpago = ActualizarTarjetaForm(request.POST)
        if form_actualizarpago.is_valid():
            tarjeta = get_object_or_404(PagoTarjeta, pk=form_actualizarpago.cleaned_data['id'])
            tarjeta.nombrepropietario = form_actualizarpago.cleaned_data['nombrepropietario']
            tarjeta.numtarjeta = form_actualizarpago.cleaned_data['numtarjeta']
            tarjeta.codseguridad = form_actualizarpago.cleaned_data['codseguridad']
            tarjeta.cuotas = form_actualizarpago.cleaned_data['cuotas']
            tarjeta.valor = form_actualizarpago.cleaned_data['valor'] 
            tarjeta.save()
            return HttpResponseRedirect(reverse("index"))


#Habitación

def actualizarhabitacion(request, identificador=''):
    
    if request.method == "GET":
        habitacion = get_object_or_404(Habitacion, pk=int(identificador))
        initial = {
            "id": habitacion.id,
            "numhabitacion": habitacion.numhabitacion,
            "tipohabitacion": habitacion.tipohabitacion,
            "canthuespedes": habitacion.canthuespedes,
            "condicion": habitacion.condicion,
        }

        form_actualizarhabitacion = ActualizarHabitacionForm(initial=initial)
        return render(request, 'recepcion/carga_habitacion.html', {'form': form_actualizarhabitacion, 'actualizar_habitacion': True})

    elif request.method == "POST":
        form_actualizarhabitacion = ActualizarHabitacionForm(request.POST)
        if form_actualizarhabitacion.is_valid():
            habitacion = get_object_or_404(Habitacion, pk=form_actualizarhabitacion.cleaned_data['id'])
            habitacion.numhabitacion = form_actualizarhabitacion.cleaned_data['numhabitacion']
            habitacion.tipohabitacion = form_actualizarhabitacion.cleaned_data['tipohabitacion']
            habitacion.canthuespedes = form_actualizarhabitacion.cleaned_data['canthuespedes']
            habitacion.condicion = form_actualizarhabitacion.cleaned_data['condicion']
            habitacion.save()
            return HttpResponseRedirect(reverse("index"))

#FUNCIONBUSCAR 

def buscarhuesped(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_buscarhuesped = BuscarhuespedForm(request.GET)
        if form_buscarhuesped.is_valid():
            huespedes = Huesped.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'recepcion/index.html', {"huespedes": huespedes, "resultados_busqueda_huesped":True})

    elif request.method == "GET":
        form_buscarhuesped = BuscarhuespedForm()
        return render(request, 'recepcion/buscar_huesped.html', {"form_buscarhuesped": form_buscarhuesped}) 

def buscarpagotarjeta(request):
    if request.method == "GET":
        form_buscarpagotarjeta = BuscarTarjetaForm()
        
        return render(request, 'recepcion/buscar_pago.html', {"form_buscarpagotarjeta": form_buscarpagotarjeta})

    elif request.method == "POST":
        form_buscarpagotarjeta = BuscarTarjetaForm(request.POST)
        if form_buscarpagotarjeta.is_valid():
            palabra_a_buscar = form_buscarpagotarjeta.cleaned_data['palabra_a_buscar'] 
            tarjetas = PagoTarjeta.objects.filter(nombre_icontains=palabra_a_buscar)
        return render(request, 'recepcion/lista_pagos.html', {"tarjetas": tarjetas})

def buscarhabitacion(request):
    if request.GET.get("numero_a_buscar") and request.method == "GET":
        form_buscarhabitacion = BuscarhuespedForm(request.GET)
        if form_buscarhabitacion.is_valid():
            habitaciones = Habitacion.objects.filter(numhabitacion__icontains=request.GET.get("numero_a_buscar"))
            return  render(request, 'recepcion/lista_habitaciones.html', {"habitaciones": habitaciones, "resultados_busqueda_habitacion":True})

    elif request.method == "GET":
        form_buscarhabitacion = BuscarHabitacionForm()
        return render(request, 'recepcion/buscar_habitacion.html', {"form_buscarhabitacion": form_buscarhabitacion}) 











