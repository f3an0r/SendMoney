from django.test import TestCase
from distribution_money.models import User
from distribution_money.serializers import DistributionMoneyFormSerializer
import json



class MainLogicAppTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(money=300.4, name='TestUser', email='test@test.net', inn=55555)
        self.user_add_1 = User.objects.create(money=100, name='TestUser',
                                              email='test1@test.net', inn=1111)
        self.user_add_1 = User.objects.create(money=300, name='TestUserAdd1',
                                              email='test2@test.net', inn=2222)
        self.user_add_1 = User.objects.create(money=200, name='TestUserAdd2',
                                              email='test3@test.net', inn=3333)

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_add_money(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '1111, 2222, 3333', 'summa': ['45'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Средства распределены')
        user = User.objects.get(inn=1111)
        self.assertEqual(user.money, 115)
        user = User.objects.get(inn=2222)
        self.assertEqual(user.money, 315)
        user = User.objects.get(inn=3333)
        self.assertEqual(user.money, 215)
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(float(user.money), 255.40)

    def test_inn_count(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '1111, 2222, 4444', 'summa': ['45'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Не все введенные ИНН есть в базе')

    def test_not_correct_summa(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '1111, 2222, 3333', 'summa': ['45000'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Не корректная сумма или недостаточно средств у пользователя')

    def test_exist_inn(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '5555, 6666, 7777', 'summa': ['45000'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Нет поьзователей с введеными inn')

    def test_correct_data_summa(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '5555, 6666, 7777', 'summa': ['45000ert'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Введены некорректные данные')

    def test_correct_data_inn(self):
        data = {'csrfmiddlewaretoken': ['xTr1HhSxrKj4J0x5GGH0szidBJYAZpGu0bsm0ZNYM8AGmBd8QEQflph4tydhUMFH'],
                'inn': '5555, 6666wer, 7777', 'summa': ['45000ert'], 'users':['{}'.format(self.user.pk)]}
        resp = self.client.post('/distribution_money/', data=data)
        # print(type(resp.content['msg']))
        response = json.loads(resp.content)
        self.assertEqual(response['msg'], 'Введены некорректные данные')


    #


