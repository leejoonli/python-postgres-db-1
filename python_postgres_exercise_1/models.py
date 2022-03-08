from re import M
from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='countries')

    def __str__(self):
        return self.name

class Location(models.Model):
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return (f'{self.street_address}, {self.city}, {self.state_province} {self.postal_code}')

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager_id = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name