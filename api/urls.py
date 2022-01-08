from django.urls import path, include
from rest_framework import routers

from api.views import TutorialViewSet

router = routers.DefaultRouter()
router.register(r'tutorials', TutorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
