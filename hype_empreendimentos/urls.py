from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from HBM_plus.views import HeartBeatMonitorPlusViewSet

HBM_plus_router = routers.DefaultRouter()
HBM_plus_router.register(
    "HBM_plus", HeartBeatMonitorPlusViewSet, basename="Heart beat monitor plus")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(HBM_plus_router.urls)),
]
