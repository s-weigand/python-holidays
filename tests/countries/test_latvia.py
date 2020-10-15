from datetime import date
import unittest

import holidays


class TestLatvia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LV()

    def test_2020(self):
        # https://www.officeholidays.com/countries/latvia/2020
        # https://en.wikipedia.org/wiki/Public_holidays_in_Latvia
        # https://likumi.lv/ta/id/72608-par-svetku-atceres-un-atzimejamam-dienam
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2020, 4, 13), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 4), self.holidays)
        self.assertIn(date(2020, 6, 23), self.holidays)
        self.assertIn(date(2020, 6, 24), self.holidays)
        self.assertIn(date(2020, 11, 18), self.holidays)
        self.assertIn(date(2020, 12, 24), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 26), self.holidays)
        self.assertIn(date(2020, 12, 31), self.holidays)
