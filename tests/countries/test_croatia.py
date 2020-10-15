from datetime import date
import unittest

import holidays


class TestCroatia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HR()

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 4, 1), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 6, 25), self.holidays)
        self.assertIn(date(2018, 8, 15), self.holidays)
        self.assertIn(date(2018, 10, 8), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)
        self.assertIn(date(2020, 11, 18), self.holidays)
