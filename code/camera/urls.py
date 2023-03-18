from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'video', views.VideoViewSet)
router.register(r'camera', views.CameraViewSet)
router.register(r'scanner', views.ScannerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]