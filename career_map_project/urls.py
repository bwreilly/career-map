from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'career_map_project.views.home', name='home'),
    url(r'', include('projection_app.urls')),
)
