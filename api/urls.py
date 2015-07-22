from django.conf.urls import url
from api.views.speaker_views import SpeakerList


urlpatterns = (
    url(r'^/speakers$', SpeakerList.as_view(), name='speakers_list'),
)
