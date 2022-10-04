from rest_framework.serializers import ModelSerializer, SlugRelatedField
from . import models

class FrameSerializer(ModelSerializer):
    columns = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = models.Frame
        fields = ('id', 'title', 'columns')

class ColumnSerializer(ModelSerializer):
    tasks = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = models.Column
        fields = ('id', 'title', 'position', 'tasks', 'frame')

class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'title', 'position', 'description', 'column')

class TaskDetailedSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

class ColumnDetailedSerializer(ModelSerializer):
    tasks = TaskDetailedSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Column
        fields = '__all__'

class FrameDetailedSerializer(ModelSerializer):
    columns = ColumnDetailedSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Frame
        fields = '__all__'