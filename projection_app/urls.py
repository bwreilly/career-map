from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
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

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^$', 'projection_app.views.index', name='index'),
)
