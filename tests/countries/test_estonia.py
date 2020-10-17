# -*- coding: utf-8 -*-
from itertools import product
from datetime import date, datetime
import unittest

import holidays


class TestES(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ES()
        self.prov_holidays = {prov: holidays.ES(prov=prov) for prov in holidays.ES.PROVINCES}

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),
            (1, 6),
            (5, 1),
            (8, 15),
            (10, 12),
            (11, 1),
            (12, 6),
            (12, 8),
            (12, 25),
        )
        for y, (m, d) in product(range(1950, 2050), fixed_days_whole_country):
            self.assertIn(date(y, m, d), self.holidays)

    def test_variable_days_in_2016(self):
        for prov, prov_holidays in self.prov_holidays.items():
            self.assertEqual(date(2016, 3, 24) in prov_holidays, prov not in ["CT", "VC"])
            self.assertEqual(date(2016, 3, 25) in prov_holidays, prov not in ["CT", "VC"])
            self.assertEqual(
                date(2016, 3, 28) in prov_holidays,
                prov in ["CT", "PV", "NC", "VC", "IB", "CM"],
            )

    def test_province_specific_days(self):
        province_days = {
            (2, 28): ["AN", "CB", "CM"],
            (3, 1): ["IB"],
            (4, 23): ["AR", "CL"],
            (5, 30): ["CN"],
            (5, 2): ["MD"],
            (6, 9): ["MC", "RI"],
            (7, 25): ["GA"],
            (9, 8): ["AS", "EX"],
            (9, 11): ["CT"],
            (9, 27): ["NC"],
            (10, 9): ["VC"],
            (10, 25): ["PV"],
        }
        for prov, prov_holidays in self.prov_holidays.items():
            for year in range(2010, 2025):
                self.assertEqual(date(year, 12, 26) in prov_holidays, prov in ["CT", "IB"])
                if year < 2015:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov
                        in [
                            "AR",
                            "CL",
                            "CM",
                            "EX",
                            "GA",
                            "MD",
                            "ML",
                            "MC",
                            "NC",
                            "PV",
                            "VC",
                        ],
                    )
                elif year == 2015:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["CM", "MD", "ML", "MC", "NC", "PV", "VC"],
                    )
                elif year == 2016:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["ML", "MC", "PV", "VC"],
                    )
                elif year == 2017:
                    self.assertEqual(date(year, 3, 19) in prov_holidays, prov in ["PV"])
                elif 2018 <= year <= 2019:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["GA", "MC", "NC", "PV", "VC"],
                    )
                elif year == 2020:
                    self.assertEqual(
                        date(year, 3, 19) in prov_holidays,
                        prov in ["CM", "GA", "MC", "NC", "PV", "VC"],
                    )
                self.assertEqual(date(year, 6, 24) in prov_holidays, prov in ["CT", "GA", "VC"])
                for fest_day, fest_prov in province_days.items():
                    self.assertEqual(date(year, *fest_day) in prov_holidays, prov in fest_prov)


class TestEstonia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.EE()
        self.cur_date = datetime.now()

    def test_new_years(self):
        test_date = date(self.cur_date.year, 1, 1)
        self.assertEqual(self.holidays.get(test_date), "uusaasta")
        self.assertIn(test_date, self.holidays)

    def test_independence_day(self):
        test_date = date(self.cur_date.year, 2, 24)
        self.assertEqual(self.holidays.get(test_date), "iseseisvuspäev")
        self.assertIn(test_date, self.holidays)

    def test_good_friday(self):
        test_date = date(2019, 4, 19)
        self.assertEqual(self.holidays.get(test_date), "suur reede")
        self.assertIn(test_date, self.holidays)

    def test_easter_sunday(self):
        test_date = date(2019, 4, 21)
        self.assertEqual(self.holidays.get(test_date), "ülestõusmispühade 1. püha")
        self.assertIn(test_date, self.holidays)

    def test_spring_day(self):
        test_date = date(self.cur_date.year, 5, 1)
        self.assertEqual(self.holidays.get(test_date), "kevadpüha")
        self.assertIn(test_date, self.holidays)

    def test_pentecost(self):
        test_date = date(2019, 6, 9)
        self.assertEqual(self.holidays.get(test_date), "nelipühade 1. püha")
        self.assertIn(test_date, self.holidays)

    def test_victory_day(self):
        test_date = date(self.cur_date.year, 6, 23)
        self.assertEqual(self.holidays.get(test_date), "võidupüha")
        self.assertIn(test_date, self.holidays)

    def test_midsummers_day(self):
        test_date = date(self.cur_date.year, 6, 24)
        self.assertEqual(self.holidays.get(test_date), "jaanipäev")
        self.assertIn(test_date, self.holidays)

    def test_restoration_of_independence_day(self):
        test_date = date(self.cur_date.year, 8, 20)
        self.assertEqual(self.holidays.get(test_date), "taasiseseisvumispäev")
        self.assertIn(test_date, self.holidays)

    def test_christmas_eve(self):
        test_date = date(self.cur_date.year, 12, 24)
        self.assertEqual(self.holidays.get(test_date), "jõululaupäev")
        self.assertIn(test_date, self.holidays)

    def test_christmas_day(self):
        test_date = date(self.cur_date.year, 12, 25)
        self.assertEqual(self.holidays.get(test_date), "esimene jõulupüha")
        self.assertIn(test_date, self.holidays)

    def test_boxing_day(self):
        test_date = date(self.cur_date.year, 12, 26)
        self.assertEqual(self.holidays.get(test_date), "teine jõulupüha")
        self.assertIn(test_date, self.holidays)
