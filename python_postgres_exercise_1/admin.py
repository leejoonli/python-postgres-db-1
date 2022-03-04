from django.contrib import admin
from .models import Region, Countries, Locations

# Register your models here.
admin.site.register(Region)
admin.site.register(Countries)
admin.site.register(Locations)