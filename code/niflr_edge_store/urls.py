from django.urls import include, path
from rest_framework import routers
from camera import urls as camera_urls 
from iot import urls as iot_urls
from ticket import urls as ticket_urls
from user import urls as user_urls
from django.contrib import admin

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include(camera_urls)),
    path('', include(iot_urls)),
    path('', include(ticket_urls)),
    path('', include(user_urls)),  
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
]
