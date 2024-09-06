from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentAccountViewSet, TransactionViewSet, AdminTransactionViewSet

router = DefaultRouter()
router.register(r'investment-accounts', InvestmentAccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'admin-transactions', AdminTransactionViewSet, basename='admin-transactions')

urlpatterns = [
    path('', include(router.urls)),
]
