from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AirportInfoSerializer, AirportDistanceSerializer
from .models import AirportDistance, AirportInfo

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/airport-list/',
		'Search by Name':'/airport-name/<str:name>/',
		'Search by City':'/airport-city/<str:city>/',
		'Search by Country':'/airport-country/<str:country>/',
		'Search by IATA':'/airport-IATA/<str:IATA>/',
		'Search by ICAO':'/airport-ICAO/<str:ICAO>/',

        'Search distance by routeCode':'/airport-distance/<str:routeCode>/'
		}

	return Response(api_urls)

@api_view(['GET'])
def airportList(request):
	airports = AirportInfo.objects.all().order_by('-id')
	serializer = AirportInfoSerializer(airports, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def airportName(request, name):
	airport = AirportInfo.objects.filter(name=name)
	serializer = AirportInfoSerializer(airport, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def airportCity(request, city):
	airport = AirportInfo.objects.get(city=city)
	serializer = AirportInfoSerializer(airport, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def airportCountry(request, country):
    airport = AirportInfo.objects.filter(country=country)
    serializer = AirportInfoSerializer(airport, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def airportIATA(request, IATA):
    airport = AirportInfo.objects.get(IATA=IATA)
    serializer = AirportInfoSerializer(airport, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def airportICAO(request, ICAO):
    airport = AirportInfo.objects.get(ICAO=ICAO)
    serializer = AirportInfoSerializer(airport, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def airportDistance(request, routeCode):
    airport = AirportDistance.objects.get(routeCode=routeCode)
    serializer = AirportDistanceSerializer(airport, many=False)
    return Response(serializer.data)




