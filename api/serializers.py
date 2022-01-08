from rest_framework import serializers

from api.models import Tutorial


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'description', 'published']
