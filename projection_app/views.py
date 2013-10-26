from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets

from models import State, Occupation



def index(request):
    return render_to_response('map.html', context_instance=RequestContext(request))


class StateViewSet(viewsets.ModelViewSet):
    model = State
    paginate_by = 50


class OccupationViewSet(viewsets.ModelViewSet):
    model = Occupation
    paginate_by = 50