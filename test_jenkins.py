import unittest
import timeFormat


class TestFormat(unittest.TestCase):
    def test_min(self):
        res = timeFormat.formatTime(60)
        self.assertEqual(res, '00:01:00')

    def test_hour(self):
        res = timeFormat.formatTime(3600)
        self.assertEqual(res, '01:00:00')

    def test_111(self):
        res = timeFormat.formatTime(3661)
        self.assertEqual(res, '01:01:01')

    def test_limit(self):
        res = timeFormat.formatTime(215999)
        self.assertEqual(res, '59:59:59')

    def test_negative(self):
        res = timeFormat.formatTime(-215999)
        self.assertEqual(res, 'Invalid Time')

    def test_nonNumeric(self):
        res = timeFormat.formatTime('okay')
        self.assertEqual(res, 'Invalid Time')


if __name__ == "__main__":
    unittest.main()
