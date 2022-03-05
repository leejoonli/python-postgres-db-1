from rest_framework import serializers
from .models import Region

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.HyperlinkedRelatedField(view_name='region_detail', read_only=True)
    class Meta:
        model = Region
        fields = ('id', 'name', 'region')