from django.contrib import admin
from .models import Region, Country, Location, Department, Job, Employee, JobHistory

# Register your models here.
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Employee)
admin.site.register(JobHistory)