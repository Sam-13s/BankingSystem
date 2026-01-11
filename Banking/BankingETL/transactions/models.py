# transactions/models.py

from django.db import models
from accounts.models import Account  # Import Account model

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    from_account = models.ForeignKey(Account, related_name='from_account', on_delete=models.CASCADE, null=True, blank=True)
    to_account = models.ForeignKey(Account, related_name='to_account', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    method = models.CharField(choices=[('ATM', 'ATM'), ('ONLINE', 'Online'), ('BRANCH', 'Branch')], default='ONLINE', max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'

