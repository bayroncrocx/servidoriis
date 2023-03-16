from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from general.models import Usuarios
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InsumosOficinaSerializador
from oficina.models import InsumosOficina
from vehiculo.models import Vehiculo
from .serializers import VehiculosSerializador
from .serializers import InsumosComputacionalesSerializador
from computacion.models import InsumosComputacionales
from rest_framework import status
from django.http import Http404

# Create your views here.

class Insumo_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        insumo = InsumosOficina.objects.all()
        serializador = InsumosOficinaSerializador(insumo, many=True)

        return Response(serializador.data)

    def post(self, request, format=None):
        serializador = InsumosOficinaSerializador(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)



class Insumo_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return InsumosOficina.objects.get(pk=pk)
        except InsumosOficina.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        insumo = self.get_object(pk)
        serializador = InsumosOficinaSerializador(insumo)
        return Response(serializador.data)

    def put(self, request, pk, format = None):
        insumo = self.get_object(pk)
        serializador = InsumosOficinaSerializador(insumo, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        insumo = self.get_object(pk)
        insumo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Vehiculo_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        vehiculo = Vehiculo.objects.all()
        serializador = VehiculosSerializador(vehiculo, many=True)

        return Response(serializador.data)

    def post(self, request, format=None):
        serializador = VehiculosSerializador(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)

class Vehiculo_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        serializador = VehiculosSerializador(vehiculo)
        return Response(serializador.data)

    def put(self, request, pk, format = None):
        vehiculo = self.get_object(pk)
        serializador = VehiculosSerializador(vehiculo, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehiculo = self.get_object(pk)
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def inicio(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion != 'Activa':
            sesion = None
    except:
        sesion = None
        return render(request, 'login.html')
    return render(request, 'index.html')

def login(request):
    return render(request,"login.html")

def iniciar_sesion(request):
    msj = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = Usuarios.objects.get(username = username, password = password)
        except:
            usuario = None

        if usuario != None:
            request.session["sesion_activa"] = "Activa"
            request.session["perfil"] = usuario.perfil
            return redirect('inicio')
        else:
            msj ='Las credenciales son incorrectas'
            return render(request, 'login.html', {'msj':msj})

def cerrar_sesion(request):
    try:
        if request.session['sesion_activa'] == 'Activa':
            del request.session['sesion_activa']
            del request.session['perfil']
            return render(request,"login.html")
        else:
            return render(request,"iniciar_sesion.html")
    except:
        return render(request,"iniciar_sesion.html")




class Computacional_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        compu = InsumosComputacionales.objects.all()
        serializador = InsumosComputacionalesSerializador(compu, many=True)

        return Response(serializador.data)

    def post(self, request, format=None):
        compu = InsumosComputacionalesSerializador(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)

class Computacional_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return InsumosComputacionales.objects.get(pk=pk)
        except compu.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        compu = self.get_object(pk)
        serializador = InsumosComputacionalesSerializador(vehiculo)
        return Response(serializador.data)

    def put(self, request, pk, format = None):
        compu = self.get_object(pk)
        serializador = InsumosComputacionalesSerializador(compu, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        compu = self.get_object(pk)
        compu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)