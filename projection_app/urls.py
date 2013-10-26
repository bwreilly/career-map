from django.conf.urls import patterns, include, url
from rest_framework import routers

from views import StateViewSet, OccupationViewSet

router = routers.DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'occupations', OccupationViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
	url(r'^$', 'projection_app.views.index', name='index'),
)
