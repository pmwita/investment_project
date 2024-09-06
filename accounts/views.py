from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime
from .models import InvestmentAccount, Transaction, UserInvestment
from .serializers import InvestmentAccountSerializer, TransactionSerializer, UserInvestmentSerializer

class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()
    serializer_class = InvestmentAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return InvestmentAccount.objects.all()
        else:
            return InvestmentAccount.objects.filter(users=user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Filter transactions based on user access
        if user.is_superuser:
            return Transaction.objects.all()
        else:
            return Transaction.objects.filter(user=user)

class AdminTransactionViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['get'])
    def user_transactions(self, request):
        user = request.user
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date and end_date:
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            transactions = Transaction.objects.filter(
                user=user,
                date__range=(start_date, end_date)
            )
        else:
            transactions = Transaction.objects.filter(user=user)
        
        total_balance = transactions.aggregate(total=models.Sum('amount'))['total'] or 0
        
        return Response({
            'transactions': TransactionSerializer(transactions, many=True).data,
            'total_balance': total_balance
        })
