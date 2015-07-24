from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = (
    url(r'^$', 'project.views.home', name='home'),
    url(r'^/api', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
