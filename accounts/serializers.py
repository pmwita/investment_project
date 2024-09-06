from rest_framework import serializers
from .models import InvestmentAccount, Transaction, UserInvestment

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class InvestmentAccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    
    class Meta:
        model = InvestmentAccount
        fields = '__all__'

class UserInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInvestment
        fields = '__all__'
