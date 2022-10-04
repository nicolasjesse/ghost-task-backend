from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from . import models, serializers


class FrameViewSet(ModelViewSet):

    serializer_class = serializers.FrameSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.FrameDetailedSerializer
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        return models.Frame.objects.all()


class ColumnViewSet(ModelViewSet):

    serializer_class = serializers.ColumnSerializer

    def create(self, request, *args, **kwargs):
        request.data["position"] = len(get_object_or_404(
            models.Frame, pk=request.data["frame"]).columns.all())
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return models.Column.objects.all()


class TaskViewSet(ModelViewSet):

    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.all()
