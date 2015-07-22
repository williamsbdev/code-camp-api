from rest_framework import serializers

from api.models.speaker import Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
