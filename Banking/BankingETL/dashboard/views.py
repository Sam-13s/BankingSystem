from django.shortcuts import render
from customers.models import Customer
from accounts.models import Account
from transactions.models import Transaction

def dashboard_view(request):
    total_customers = Customer.objects.count()
    total_accounts = Account.objects.count()
    total_transactions = Transaction.objects.count()
    recent_transactions = Transaction.objects.order_by('-timestamp')[:5]
    context = {
        'total_customers': total_customers,
        'total_accounts': total_accounts,
        'total_transactions': total_transactions,
        'recent_transactions': recent_transactions,
    }
    return render(request, 'dashboard/dashboard.html', context)
