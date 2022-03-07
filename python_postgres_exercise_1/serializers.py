from rest_framework import serializers
from .models import Region, Country, Location

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