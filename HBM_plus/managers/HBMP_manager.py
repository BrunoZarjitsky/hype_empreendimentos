from django.utils import timezone
from math import pi, cos, sin, trunc


class HeartBeatMonitorPlusManager:
    def __init__(self):
        self.monitor_equation = "-0.06366 + 0.12613 * cos(pi*timestamp/500) + 0.12258 * cos(pi*timestamp/250)"\
            " + 0.01593 * sin(pi*timestamp/500) + 0.03147 * sin(pi*timestamp/250)"

    def read_monitor(self):
        current_timestamp = self._get_current_timestamp()
        return self._calculate_HBMP(current_timestamp)

    @staticmethod
    def _get_current_timestamp():
        return trunc(timezone.now().timestamp() * 1000)

    def _calculate_HBMP(self, timestamp: float) -> float:
        return eval(self.monitor_equation)
