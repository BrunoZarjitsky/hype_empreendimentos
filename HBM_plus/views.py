from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from HBM_plus.managers.HBMP_manager import HeartBeatMonitorPlusManager


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
