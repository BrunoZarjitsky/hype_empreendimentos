from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from HBM_plus.managers.HBMP_manager import HeartBeatMonitorPlusManager
from HBM_plus.scripts.stress_test_api import StressTestManager
from time import time


class HeartBeatMonitorPlusViewSet(ViewSet):
    @action(detail=False, methods=["GET"], url_path="read_heart_beat_monitor")
    def get_heart_beat_monitor(self, request):
        try:
            manager = HeartBeatMonitorPlusManager()
            return Response(
                data={
                    "value": manager.read_monitor(),
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                data={
                    "message": "Unexpected error",
                    "detail": str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class StressTestViewSet(ViewSet):
    @action(detail=False, methods=["GET"], url_path="run_stress_test")
    def get_stress_test_results(self, request):
        try:
            initial_time = time()
            time_testing_in_seconds = int(request.data.get(
                "time_testing_in_seconds", 1))
            manager = StressTestManager(time_testing_in_seconds)
            return Response(
                data=manager.get_stress_test_results(),
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                data={
                    "message": "Unexpected error",
                    "detail": str(error),
                    "time_runned": time() - initial_time,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
