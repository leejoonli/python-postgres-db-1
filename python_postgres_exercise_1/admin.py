from django.contrib import admin
from .models import Region, Country, Locations

# Register your models here.
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Locations)