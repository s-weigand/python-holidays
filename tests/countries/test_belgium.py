# -*- coding: utf-8 -*-
from datetime import date
import unittest

import holidays


class TestBelgium(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BE()

    def test_2017(self):
        # https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 7, 21), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 11, 11), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
