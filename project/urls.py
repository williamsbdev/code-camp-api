from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = (
    url(r'^$', 'project.views.home', name='home'),
    url(r'^/api', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
