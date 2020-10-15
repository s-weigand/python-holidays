from datetime import date
import unittest

import holidays


class TestChile(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Chile()

    def test_2019(self):
        # No laborables (sector público) not included
        self.assertIn(date(2019, 1, 1), self.holidays)
        # self.assertIn(date(2019, 4, 18), self.holidays)
        self.assertIn(date(2019, 4, 19), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 21), self.holidays)
        self.assertIn(date(2019, 6, 29), self.holidays)
        self.assertIn(date(2019, 7, 16), self.holidays)
        self.assertIn(date(2019, 8, 15), self.holidays)
        self.assertIn(date(2019, 9, 18), self.holidays)
        self.assertIn(date(2019, 9, 19), self.holidays)
        self.assertIn(date(2019, 9, 20), self.holidays)
        self.assertIn(date(2009, 10, 12), self.holidays)
        self.assertIn(date(2019, 10, 12), self.holidays)
        self.assertIn(date(2019, 11, 1), self.holidays)
        self.assertIn(date(2019, 12, 8), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
