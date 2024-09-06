from django.test import TestCase
from django.contrib.auth.models import User
from .models import InvestmentAccount, Transaction, UserInvestment

class InvestmentAccountTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.account = InvestmentAccount.objects.create(name='Test Account')
        UserInvestment.objects.create(user=self.user, account=self.account, access_level=UserInvestment.FULL_ACCESS)
    
    def test_user_access(self):
        self.assertTrue(UserInvestment.objects.filter(user=self.user, account=self.account).exists())
