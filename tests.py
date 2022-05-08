from django.test import TestCase
from account.views import registration_view, logout_view, login_view, account_view


class Test_account(unittest.TestCase):
    def create_registration_view(self):
        return account.views.create(email='vikush40@gmail.com', raw_password='medical7')

    def test_registration_view(self):
        a = self.create_registration_view()
        self.assertTrue(isinstance(a, account))
        self.assertEqual(a.__unicode__(), a.email)
