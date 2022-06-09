from django import forms

#Agregar

class AgregarhuespedForm(forms.Form):
    nombre = forms.CharField(label= "Nombre", max_length=100)
    apellido = forms.CharField(label= "Apellido", max_length=100)
    documento = forms.IntegerField(label= "Documento")
    email = forms.EmailField(label= "Email", max_length=100)
    formadepago = forms.CharField(label= "Forma de pago", max_length=100)

class AgregarPagoForm(forms.Form):
    nombrepropietario = forms.CharField(label= "Nombre de Titular")
    numtarjeta = forms.IntegerField(label= "Nro. de Tarjeta")
    codseguridad = forms.IntegerField(label= "Codigo de Seguridad")
    cuotas = forms.IntegerField(label= "Cantidad de Cuotas")
    valor = forms.FloatField(label= "Valor de Cuota")  

class AgregarHabitacionForm(forms.Form):
    numhabitacion = forms.IntegerField(label= "Nro. de habitacion")
    tipohabitacion = forms.CharField(label= "Habitacion Doble/Triple/Cuadruple", max_length=100)
    canthuespedes = forms.IntegerField(label= "Cantidad de Huespedes")
    condicion = forms.CharField(label= "Libre/Ocupado", max_length=100)      

#Actualizar

class ActualizarhuespedForm(AgregarhuespedForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

class ActualizarTarjetaForm(AgregarPagoForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

class ActualizarHabitacionForm(AgregarHabitacionForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

#Buscar

class BuscarhuespedForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar Huesped", max_length=100) 

class BuscarTarjetaForm(forms.Form):
    palabras_a_buscar = forms.CharField(label="Buscar Por Nombre de Propietario", max_length=100)

class BuscarHabitacionForm(forms.Form):
    numero_a_buscar = forms.CharField(label="Buscar Habitacion", max_length=100)


  
