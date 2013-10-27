from django.conf.urls import patterns, include, url
from rest_framework import routers

from views import (
	# StateViewSet,
	OccupationViewSet,
	NameViewSet,
)

router = routers.DefaultRouter()
# router.register(r'states', StateViewSet)
router.register(r'occupations', OccupationViewSet)
router.register(r'names', NameViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
	url(r'^$', 'projection_app.views.index', name='index'),
)
