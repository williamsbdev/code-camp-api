from rest_framework import generics

from api.models.speaker import Speaker
from api.serializers.speaker_serializer import SpeakerSerializer


class SpeakerList(generics.ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
