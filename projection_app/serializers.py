import json

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from models import Occupation, State, Name


class OccupationSerializer(serializers.HyperlinkedModelSerializer):
    area_name = SlugRelatedField(slug_field='state_name')

    class Meta:
        model = Occupation


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ('name',)


class StateSerializer(serializers.HyperlinkedModelSerializer):
    geometry = serializers.SerializerMethodField('get_geojson')

    def get_geojson(self, obj):
        return json.loads(obj.geometry.geojson)

    class Meta:
        model = State
        fields = ('url', 'state_name', 'geometry')
