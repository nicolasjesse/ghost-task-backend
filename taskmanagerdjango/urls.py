from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks import viewsets as tasks

router = routers.DefaultRouter()

router.register(r'frames', tasks.FrameViewSet, basename='api-frames')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
