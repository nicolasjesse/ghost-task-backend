from rest_framework.serializers import ModelSerializer
from . import models

class FrameSerializer(ModelSerializer):
    class Meta:
        model = models.Frame
        fields = '__all__'

