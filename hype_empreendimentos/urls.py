from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from HBM_plus.views import (
    HeartBeatMonitorPlusViewSet,
    StressTestViewSet,
)

HBM_plus_router = routers.DefaultRouter()
HBM_plus_router.register(
    "HBM_plus", HeartBeatMonitorPlusViewSet, basename="Heart beat monitor plus")

stress_test_router = routers.DefaultRouter()
stress_test_router.register(
    "stress_test", StressTestViewSet, basename="stress_test_router"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(HBM_plus_router.urls)),
    path('', include(stress_test_router.urls)),
]
