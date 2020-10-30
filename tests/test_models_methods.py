from django.test import TestCase
from distribution_money.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(money=300.4, name='TestUser', email='test@test.net', inn=55555)

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_add_money(self):
        self.user.add_money(30)
        self.assertEqual(self.user.money, 330.4)

    def test_get_money_yes(self):
        self.user.get_money(30)
        self.assertEqual(self.user.money, 270.4)

    def test_get_money_no(self):
        status = self.user.get_money(5000)
        self.assertFalse(status)
