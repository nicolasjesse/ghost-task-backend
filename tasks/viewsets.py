from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from . import models, serializers

class FrameViewSet(ModelViewSet):
    
    serializer_class = serializers.FrameSerializer

    def get_queryset(self):
        return models.Frame.objects.all()