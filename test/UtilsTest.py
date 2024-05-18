import unittest
from src import utils


class UtilsTest(unittest.TestCase):
    ts = 5
    window_size = 10
    window = utils.get_window(
        timestamp=ts,
        window_range=window_size
    )

    def test_window_range(self):
        self.assertEqual(self.window_size, self.window[1] - self.window[0] + 1)

    def test_timestamp_within_window(self):
        self.assertTrue(self.ts >= self.window[0] & self.ts <= self.window[1])

    ts = 5
    window_size = 5
    window = utils.get_window(
        timestamp=ts,
        window_range=window_size
    )

    def test_window_range_2(self):
        self.assertEqual(self.window_size, self.window[1] - self.window[0] + 1)

    def test_timestamp_within_window_2(self):
        self.assertTrue(self.ts >= self.window[0] & self.ts <= self.window[1])


if __name__ == '__main__':
    unittest.main()
