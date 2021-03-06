from rest_framework import serializers
from .models import Region, Country, Location, Department, Job, Employee, JobHistory

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.HyperlinkedRelatedField(view_name='region_detail', read_only=True)
    region_url = serializers.ModelSerializer.serializer_url_field(view_name='region_detail')
    class Meta:
        model = Region
        fields = ('id', 'name', 'region', 'region_url')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.HyperlinkedRelatedField(view_name='region_detail', read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(),
        source='region'
    )
    # country = serializers.HyperlinkedRelatedField(view_name='country_detail', read_only = True)
    country_url = serializers.ModelSerializer.serializer_url_field(view_name='country_detail')
    class Meta:
        model = Country
        fields = ('id', 'name', 'region', 'region_id', 'country_url')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.HyperlinkedRelatedField(view_name='country_detail', read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country'
    )
    location_url = serializers.ModelSerializer.serializer_url_field(view_name='location_detail')
    class Meta:
        model = Location
        fields = ('id', 'street_address', 'postal_code', 'city', 'state_province', 'country', 'country_id', 'location_url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(view_name='location_detail', read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location'
    )
    department_url = serializers.ModelSerializer.serializer_url_field(view_name='department_detail')
    class Meta:
        model = Department
        fields = ('id', 'name', 'manager_id', 'location', 'location_id', 'department_url')

class JobSerializer(serializers.HyperlinkedModelSerializer):
    job_url = serializers.ModelSerializer.serializer_url_field(view_name='job_detail')
    class Meta:
        model = Job
        fields = ('id', 'job_title', 'min_salary', 'max_salary', 'job_url')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.HyperlinkedRelatedField(view_name='job_detail', read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(),
        source='job'
    )
    department = serializers.HyperlinkedRelatedField(view_name='department_detail', read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department'
    )
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job', 'job_id', 'salary', 'manager_id', 'department', 'department_id')

class JobHistorySerializer(serializers.HyperlinkedModelSerializer):
    employee = serializers.HyperlinkedRelatedField(view_name='employee_detail', read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='employee'
    )
    job = serializers.HyperlinkedRelatedField(view_name='job_detail', read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(),
        source='job'
    )
    department = serializers.HyperlinkedRelatedField(view_name='department_detail', read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='deparment'
    )
    class Meta:
        model = JobHistory
        fields = ('id', 'employee', 'employee_id', 'start_date', 'end_date', 'job', 'job_id', 'department', 'department_id')