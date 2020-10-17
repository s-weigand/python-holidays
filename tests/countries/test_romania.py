# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestRomania(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.RO()

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Romania
        # https://publicholidays.ro/2020-dates/
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 2), self.holidays)
        self.assertIn(date(2020, 1, 24), self.holidays)
        self.assertIn(date(2020, 4, 17), self.holidays)
        self.assertIn(date(2020, 4, 19), self.holidays)
        self.assertIn(date(2020, 4, 20), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 6, 1), self.holidays)
        self.assertIn(date(2020, 6, 7), self.holidays)
        self.assertIn(date(2020, 6, 8), self.holidays)
        self.assertIn(date(2020, 8, 15), self.holidays)
        self.assertIn(date(2020, 11, 30), self.holidays)
        self.assertIn(date(2020, 12, 1), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 26), self.holidays)

    def test_children_s_day(self):
        #  Children’s Day became an official Romanian public holiday in 2017.
        self.assertNotIn(date(2016, 6, 1), self.holidays)
        self.assertIn(date(2017, 6, 1), self.holidays)
