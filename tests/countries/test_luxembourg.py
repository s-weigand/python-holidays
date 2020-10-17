from datetime import date
import unittest

import holidays


class TestLU(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LU()

    def test_2019(self):
        # https://www.officeholidays.com/countries/luxembourg/2019
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 4, 22), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 9), self.holidays)
        self.assertIn(date(2019, 5, 30), self.holidays)
        self.assertIn(date(2019, 6, 10), self.holidays)
        self.assertIn(date(2019, 6, 23), self.holidays)
        self.assertIn(date(2019, 8, 15), self.holidays)
        self.assertIn(date(2019, 11, 1), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertIn(date(2019, 12, 26), self.holidays)
