# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestHonduras(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HND()

    def test_2014(self):
        self.assertIn(date(2014, 10, 3), self.holidays)  # Morazan's Day
        self.assertIn(date(2014, 10, 12), self.holidays)  # Columbus Day
        self.assertIn(date(2014, 10, 21), self.holidays)  # Army Day

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)  # New Year
        self.assertIn(date(2018, 4, 14), self.holidays)  # America's Day
        self.assertIn(date(2018, 5, 1), self.holidays)  # Workers' Day
        self.assertNotIn(date(2018, 5, 6), self.holidays)  # Mother's Day
        self.assertIn(date(2018, 5, 13), self.holidays)  # Mother's Day
        self.assertIn(date(2018, 9, 10), self.holidays)  # Children weekend
        self.assertIn(date(2018, 9, 15), self.holidays)  # Independence Day
        self.assertIn(date(2018, 9, 17), self.holidays)  # Teacher's Day
        self.assertIn(date(2018, 10, 3), self.holidays)  # Morazan's weekend
        self.assertIn(date(2018, 12, 25), self.holidays)  # Christmas
