from rest_framework import serializers
from oficina.models import InsumosOficina
from computacion.models import InsumosComputacionales
from vehiculo.models import Vehiculo



class InsumosOficinaSerializador(serializers.ModelSerializer):
    class Meta:
        model = InsumosOficina
        fields = '__all__'

class InsumosComputacionalesSerializador(serializers.ModelSerializer):
    class Meta:
        model = InsumosComputacionales
        fields = '__all__'

class VehiculosSerializador(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
