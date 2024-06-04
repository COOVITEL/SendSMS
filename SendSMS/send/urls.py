from django.urls import path, include
from rest_framework import routers
from .views import SendViews

router = routers.DefaultRouter()
router.register(r'sends', SendViews, 'sends')

urlpatterns = [
    path('send/SMS/', include(router.urls))
]
