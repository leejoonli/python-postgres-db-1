from re import M
from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Countries(models.Model):
    name = models.CharField(max_length=100)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='countries')

    def __str__(self):
        return self.name

class Locations(models.Model):
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return (f'{self.street_address}, {self.city}, {self.state_province} {self.postal_code}')