from django.contrib.auth.models import User
from django.db import models

class InvestmentAccount(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='UserInvestment')

class Transaction(models.Model):
    account = models.ForeignKey(InvestmentAccount, related_name='transactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class UserInvestment(models.Model):
    VIEW_ONLY = 'view'
    FULL_ACCESS = 'full'
    POST_ONLY = 'post'

    ACCESS_CHOICES = [
        (VIEW_ONLY, 'View Only'),
        (FULL_ACCESS, 'Full Access'),
        (POST_ONLY, 'Post Only'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=10, choices=ACCESS_CHOICES)
