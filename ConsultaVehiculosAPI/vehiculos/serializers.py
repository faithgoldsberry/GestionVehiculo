from rest_framework import serializers
from .models import Vehiculo, Placa

class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placa
        fields = ['patente']

class VehiculoSerializer(serializers.ModelSerializer):
    placas = PlacaSerializer(many=True, required=False)  # Deja placas como optional

    class Meta:
        model = Vehiculo
        fields = ['vin', 'motor', 'cilindrada', 'ano', 'marca', 'modelo', 'version', 'dueno', 'placas']

    def create(self, validated_data):
        placas_data = validated_data.pop('placas', [])  # Lista vacía por defecto si no se provee placas
        vehiculo = Vehiculo.objects.create(**validated_data)
        for placa_data in placas_data:
            Placa.objects.create(vehiculo=vehiculo, **placa_data)
        return vehiculo
