from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user_session', views.UserSessionViewSet)
router.register(r'user_detail', views.UserDetailViewSet)
router.register(r'user_cycle', views.UserCycleViewSet)
router.register(r'cart', views.CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('entry-control/', views.EntryControlView.as_view(), name='entry-control'),
    path('exit-control/', views.ExitControlView.as_view(), name='exit-control'),
]