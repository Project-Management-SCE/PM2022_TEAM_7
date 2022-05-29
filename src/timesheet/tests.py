from django.test import TestCase
import timesheet.views


# Create your tests here.
class Test_timesheet(TestCase):
    def next_year_view(self):
        self.assertEqual(next_year(1), '2')
