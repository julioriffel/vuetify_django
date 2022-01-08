from rest_framework import viewsets

# Serializers define the API representation.
from api.models import Tutorial
from api.serializers import TutorialSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
