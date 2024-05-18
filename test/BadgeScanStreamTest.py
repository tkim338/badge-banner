import unittest
from src import BadgeScanStream


class BadgeScanStreamTest(unittest.TestCase):
    badge_count = 20
    event_count = 20
    duration = 120
    event_list = BadgeScanStream.generate_random_date(
        duration_sec=duration,
        num_unique_badges=badge_count,
        num_scan_events=event_count
    )

    def test_event_list_length(self):
        self.assertEqual(len(self.event_list), self.event_count)

    def test_unique_badge_count(self):
        self.assertEqual(len({e[0] for e in self.event_list}), self.badge_count)

    def test_event_list_duration(self):
        self.assertTrue(self.event_list[-1][0] - self.event_list[0][0] <= self.duration)


if __name__ == '__main__':
    unittest.main()
