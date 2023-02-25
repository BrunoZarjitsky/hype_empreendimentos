import requests
from time import time
from typing import Union
from hype_empreendimentos.settings import USED_HOST_URL
import logging

logger = logging.getLogger(__name__)


class StressTestManager:
    def __init__(self, time_testing_in_seconds: Union[int, None] = None) -> None:
        self._url = f"{USED_HOST_URL}/HBM_plus/read_heart_beat_monitor/"
        self._time_testing_in_seconds = time_testing_in_seconds if time_testing_in_seconds else 1
        self._requests = 0
        self._requests_per_second = 0
        self._stress_test_read_heart_beat_monitor_endpoint()

    def _stress_test_read_heart_beat_monitor_endpoint(self) -> None:
        initial_time = time()
        total_iterations = 0
        while (time() - initial_time) < self._time_testing_in_seconds:
            requests.get(self._url)
            total_iterations += 1
        self._requests = total_iterations
        self._requests_per_second = total_iterations / self._time_testing_in_seconds

    def get_stress_test_results(self):
        return {
            "requests": self._requests,
            "requests_per_second": self._requests_per_second,
            "time_in_seconds": self._time_testing_in_seconds
        }


if __name__ == "__main__":
    time_testing_in_seconds = input(
        'Type for how long would you like to run the stress test (in seconds): ')
    try:
        time_testing_in_seconds = int(time_testing_in_seconds)
    except:
        time_testing_in_seconds = 1
    manager = StressTestManager(time_testing_in_seconds)
    stress_test_results = manager.get_stress_test_results()
    print(f"Runned {stress_test_results.get('iterations', 0)} in {stress_test_results.get('time_in_seconds', time_testing_in_seconds)} seconds")
