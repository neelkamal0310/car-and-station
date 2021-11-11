from django.db import models

# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def vehicles(self):
        return len(self.vehicle_set.all())

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    regdno = models.CharField(max_length=100, primary_key=True)
    fuel = models.IntegerField()
    odometer = models.IntegerField()
    booked = models.BooleanField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.regdno}'
