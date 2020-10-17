# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestPeru(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Peru()

    def test_2019(self):
        # No laborables (sector público) not included
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 4, 18), self.holidays)
        self.assertIn(date(2019, 4, 19), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 6, 29), self.holidays)
        self.assertIn(date(2019, 7, 29), self.holidays)
        self.assertIn(date(2019, 8, 30), self.holidays)
        self.assertIn(date(2019, 10, 8), self.holidays)
        self.assertIn(date(2019, 11, 1), self.holidays)
        self.assertIn(date(2019, 12, 8), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
