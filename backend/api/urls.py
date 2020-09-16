from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('airport-list/', views.airportList, name="airport-list"),
    
    path('airport-name/<str:name>/', views.airportName, name="airport-name"),
    path('airport-city/<str:city>/', views.airportCity, name="airport-city"),
    path('airport-country/<str:country>/', views.airportCountry, name="airport-country"),
    
    path('airport-IATA/<str:IATA>/', views.airportIATA, name="airport-IATA"),
    path('airport-ICAO/<str:ICAO>/', views.airportICAO, name="airport-ICAO"),
    
    path('airport-distance/<str:routeCode>/', views.airportDistance, name="airport-distance"),

]