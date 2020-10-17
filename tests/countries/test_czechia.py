# -*- coding: utf-8 -*-
from datetime import date
import unittest
import warnings

import holidays


class TestCZ(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CZ()

    def test_2017(self):
        # http://www.officeholidays.com/countries/czech_republic/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 7, 5), self.holidays)
        self.assertIn(date(2017, 7, 6), self.holidays)
        self.assertIn(date(2017, 9, 28), self.holidays)
        self.assertIn(date(2017, 10, 28), self.holidays)
        self.assertIn(date(2017, 11, 17), self.holidays)
        self.assertIn(date(2017, 12, 24), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_others(self):
        self.assertIn(date(1991, 5, 9), self.holidays)

    def test_czech_deprecated(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            czech = holidays.Czech()
            self.assertIsInstance(czech, holidays.Czechia)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
