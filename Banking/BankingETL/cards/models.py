# cards/models.py

from django.db import models
from customers.models import Customer
from accounts.models import Account

class Card(models.Model):
    CARD_TYPES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('expired', 'Expired'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=10, choices=CARD_TYPES)
    card_number = models.CharField(max_length=16, unique=True)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='card')
    
    def __str__(self):
        return f"{self.card_type.title()} - {self.card_number}"
