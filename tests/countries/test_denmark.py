# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestDK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.DK()

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2016, 4, 22), self.holidays)
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 16), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)
