from datetime import date
import unittest

import holidays


class TestNigeria(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Nigeria()

    def test_fixed_holidays(self):
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 27), self.holidays)
        self.assertIn(date(2019, 6, 12), self.holidays)
        self.assertIn(date(2019, 10, 1), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertIn(date(2019, 12, 26), self.holidays)
