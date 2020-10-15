from datetime import date
import unittest

import holidays


class TestUkraine(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UA()

    def test_before_1918(self):
        self.assertNotIn(date(1917, 12, 31), self.holidays)

    def test_2018(self):
        # http://www.buhoblik.org.ua/kadry-zarplata/vremya/1676-1676-kalendar.html
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 4, 8), self.holidays)
        self.assertIn(date(2018, 5, 27), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 6, 28), self.holidays)
        self.assertIn(date(2018, 8, 24), self.holidays)
        self.assertIn(date(2018, 10, 14), self.holidays)

    def test_old_holidays(self):
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 2), self.holidays)
        self.assertIn(date(1991, 7, 16), self.holidays)
        self.assertIn(date(1950, 1, 22), self.holidays)
        self.assertIn(date(1999, 11, 7), self.holidays)
        self.assertIn(date(1999, 11, 8), self.holidays)
        self.assertIn(date(1945, 5, 9), self.holidays)
        self.assertIn(date(1945, 9, 3), self.holidays)
        self.assertIn(date(1981, 10, 7), self.holidays)
        self.assertIn(date(1937, 12, 5), self.holidays)
        self.assertIn(date(1918, 3, 18), self.holidays)
