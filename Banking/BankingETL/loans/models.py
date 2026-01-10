from django.db import models

# loans/models.py
from django.db import models
from customers.models import Customer
from accounts.models import Account

class Loan(models.Model):
    LOAN_TYPES = [
        ('home', 'Home Loan'),
        ('personal', 'Personal Loan'),
        ('car', 'Car Loan'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure_months = models.IntegerField()
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    linked_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan_type} loan for {self.customer.name}"

