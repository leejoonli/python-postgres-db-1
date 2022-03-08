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

class Job(models.Model):
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def __str__(self):
        return self.job_title

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='jobs')
    salary = models.IntegerField()
    manager_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.first_name