from rest_framework import serializers
from .models import AirportDistance, AirportInfo

class AirportInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportInfo
        fields = '__all__'


class AirportDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportDistance
        fields = '__all__'