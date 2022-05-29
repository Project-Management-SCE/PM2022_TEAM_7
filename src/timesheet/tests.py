from django.test import TestCase
import unittest

class Test_timesheet_views(unittest.TestCase)
    def test_get_date(self):
        self.assertEqual(get_date(req), datetime.today())

    def test_prev_month(self):
        self.assertEqual(prev_month(1), 2)

    def test_next_month(self):
        self.assertEqual(next_month(1), 2)

    def test_prev_year(self):
        self.assertEqual(prev_year(1), 2)

    def test_next_year(self):
        self.assertEqual(next_year(1), 2)

    
