from rest_framework import serializers
from models import Occupation, State, Name


class OccupationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occupation


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ('name',)


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('url', 'state_name', 'geometry')
