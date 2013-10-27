from rest_framework import serializers
from models import Occupation, State


class OccupationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occupation


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('url', 'state_name', 'geometry')
