from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('SAVINGS', 'Savings'),
        ('CHECKING', 'Checking'),
        ('CREDIT', 'Credit'),
        ('TRANSACTION', 'Transaction'),
        ('LOAN', 'Loan'),
        ('CARD', 'Card'),
    ]
    
    account_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='accounts')
    account_type = models.CharField(max_length=12, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_type}"
