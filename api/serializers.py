from rest_framework import serializers
from .models import Port, Trajet

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class TrajetSerializer(serializers.ModelSerializer):
    port_depart = PortSerializer()
    port_arrivee = PortSerializer()

    class Meta:
        model = Trajet
        fields = '__all__'
