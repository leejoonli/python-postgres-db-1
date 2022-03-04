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