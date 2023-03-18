from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'weight', views.WeightViewSet)
router.register(r'machine', views.MachineViewSet)
router.register(r'store_session', views.StoreSessionViewSet)
router.register(r'store_mode', views.StoreModeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/machines/heartbeat', views.HeartbeatView.as_view(), name='heartbeat'),
    path('api/machines/lock', views.lock.as_view(), name='lock'),
    path('api/machines/1644496921479/status', views.status.as_view(), name='status'),
    path('mode-control/', views.ModeControlView.as_view(), name='mode-control'),
]