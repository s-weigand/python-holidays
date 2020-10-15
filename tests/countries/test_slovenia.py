from datetime import date
import unittest

import holidays


class TestSI(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SI()

    def test_holidays(self):
        """
        Test all expected holiday dates
        :return:
        """
        # New Year
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        # Prešeren's day
        self.assertIn(date(2017, 2, 8), self.holidays)
        # Easter monday - 2016 and 2017
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        # Day of uprising against occupation
        self.assertIn(date(2017, 4, 27), self.holidays)
        # Labour day
        self.assertIn(date(2017, 5, 1), self.holidays)
        # Labour day
        self.assertIn(date(2017, 5, 2), self.holidays)
        # Statehood day
        self.assertIn(date(2017, 6, 25), self.holidays)
        # Assumption day
        self.assertIn(date(2017, 8, 15), self.holidays)
        # Reformation day
        self.assertIn(date(2017, 10, 31), self.holidays)
        # Remembrance day
        self.assertIn(date(2017, 11, 1), self.holidays)
        # Christmas
        self.assertIn(date(2017, 12, 25), self.holidays)
        # Day of independence and unity
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_non_holidays(self):
        """
        Test dates that should be excluded from holidays list
        :return:
        """
        # January 2nd was not public holiday between 2012 and 2017
        self.assertNotIn(date(2013, 1, 2), self.holidays)
        self.assertNotIn(date(2014, 1, 2), self.holidays)
        self.assertNotIn(date(2015, 1, 2), self.holidays)
        self.assertNotIn(date(2016, 1, 2), self.holidays)

    def test_missing_years(self):
        self.assertNotIn(date(1990, 1, 1), self.holidays)
