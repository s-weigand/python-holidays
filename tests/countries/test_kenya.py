# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestKenya(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Kenya()

    def test_2019(self):
        # New Year's Day
        self.assertIn(date(2019, 1, 1), self.holidays)
        # Good Friday
        self.assertIn(date(2019, 4, 19), self.holidays)
        # Easter Monday
        self.assertIn(date(2019, 4, 22), self.holidays)
        # Labour Day
        self.assertIn(date(2019, 5, 1), self.holidays)
        # Madaraka Day
        self.assertIn(date(2019, 6, 1), self.holidays)
        # Mashujaa Day
        self.assertIn(date(2019, 10, 20), self.holidays)
        # Jamhuri (Independence) Day
        self.assertIn(date(2019, 12, 12), self.holidays)
        # Christmas Day
        self.assertIn(date(2019, 12, 25), self.holidays)
        # Boxing Day
        self.assertIn(date(2018, 12, 26), self.holidays)
