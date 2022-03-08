from django.contrib import admin
from .models import Region, Country, Location, Department

# Register your models here.
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Department)