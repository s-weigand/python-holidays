from datetime import date
import unittest

import holidays


class TestRussia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.RU()

    def test_2018(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Russia
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 2), self.holidays)
        self.assertIn(date(2018, 1, 3), self.holidays)
        self.assertIn(date(2018, 1, 4), self.holidays)
        self.assertIn(date(2018, 1, 5), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 1, 8), self.holidays)
        self.assertIn(date(2018, 2, 23), self.holidays)
        self.assertIn(date(2018, 3, 8), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 6, 12), self.holidays)
        self.assertIn(date(2018, 11, 4), self.holidays)
