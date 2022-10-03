import uuid
from django.db import models

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Frame(BaseModel):

    title = models.TextField(verbose_name='Title')

class Column(BaseModel):

    title = models.TextField(verbose_name='Title')
    position = models.IntegerField(verbose_name='Position')
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, related_name='columns')

class Task(BaseModel):

    title = models.TextField(verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    position = models.IntegerField(verbose_name='Position')
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')