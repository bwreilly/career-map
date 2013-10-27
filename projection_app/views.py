from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets

from serializers import OccupationSerializer, StateSerializer
from filters import NameFilter
from models import Occupation, State, Name


def index(request):
    return render_to_response('map.html', context_instance=RequestContext(request))


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class OccupationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    filter_fields = ('name',)


class NameViewSet(viewsets.ReadOnlyModelViewSet):
    model = Name
    filter_class = NameFilter