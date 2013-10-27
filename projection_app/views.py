from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets

from serializers import OccupationSerializer, StateSerializer, NameSerializer
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
    serializer_class = NameSerializer
    queryset = Name.objects.all()
    paginate_by = 10


    def get_queryset(self):
        name = self.request.QUERY_PARAMS.get('name', None)
        queryset = self.queryset
        if name is not None:
            queryset = self.queryset.filter(name__icontains=name)
        return queryset