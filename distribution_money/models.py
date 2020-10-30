from django.db import models

class User(models.Model):
    money = models.DecimalField(max_digits=50, decimal_places=2)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    inn = models.IntegerField(null=True)

    def add_money(self, summa):
        """
        Add money for user's account
        :param summa: value for add
        :return:
        """
        self.money += summa
        self.save()

    def get_money(self, summa):
        """
        Get money from the user's account
        :param summa: the amount to be withdrawn from the account
        :return: True - if summa is get
        :return: False - if summa is not get
        """
        if not summa:
            return False
        if self.money >= summa:
            self.money -= summa
            self.save()
            return True
        else:
            return False

