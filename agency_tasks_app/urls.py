from django.urls import path, include
from rest_framework import routers

from .views import SpyCatView, MissionsView

router = routers.DefaultRouter()
router.register('spycats', SpyCatView)
router.register('missions', MissionsView)

urlpatterns = [
    path('api/', include(router.urls)),
]
