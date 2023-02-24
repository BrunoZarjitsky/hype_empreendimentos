from django.test import TestCase
from HBM_plus.managers.HBMP_manager import HeartBeatMonitorPlusManager
from time import time
from unittest import mock


def mock_initial_value(self):
    return 1677245441296


class HBMPManagerTestCase(TestCase):
    def setUp(self):
        self.initial_timestamp = 1677245441296
        self.reference_output_value = -0.20419946647182974

    def test_calculate_HBMP(self):
        manager = HeartBeatMonitorPlusManager()
        assert manager._calculate_HBMP(
            self.initial_timestamp) == self.reference_output_value

    @mock.patch("HBM_plus.managers.HBMP_manager.HeartBeatMonitorPlusManager._get_current_timestamp", mock_initial_value)
    def test_read_monitor(self):
        manager = HeartBeatMonitorPlusManager()
        assert manager.read_monitor() == self.reference_output_value

    def test_stress(self):
        manager = HeartBeatMonitorPlusManager()
        initial_time = time()
        counter = 0
        while (time() - initial_time) < 1:
            manager.read_monitor()
            counter += 1
        assert counter > 10_000
