from django.db import models

# Create your models here.

class AirportInfo(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    IATA = models.CharField(max_length=3)
    ICAO = models.CharField(max_length=4)

    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()

    timezone = models.FloatField()
    DST = models.CharField(max_length=3)
    tzDatabaseTimeZone = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AirportDistance(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    distance = models.IntegerField()

    routeCode = models.CharField(max_length=8, primary_key=True)

    def __str__(self):
        return self.routeCode