from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks import viewsets as tasks

router = routers.DefaultRouter()

router.register(r'frames', tasks.FrameViewSet, basename='api-frames')
router.register(r'columns', tasks.ColumnViewSet, basename='api-columns')
router.register(r'tasks', tasks.TaskViewSet, basename='api-tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
