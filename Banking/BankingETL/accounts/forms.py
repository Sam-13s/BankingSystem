from django import forms
from django.core.exceptions import ValidationError
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_number', 'customer', 'account_type', 'balance']
        widgets = {
            'account_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'account_type': forms.Select(choices=Account.ACCOUNT_TYPES, attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
        }

    def clean_account_number(self):
        account_number = self.cleaned_data.get('account_number')
        if Account.objects.filter(account_number=account_number).exists():
            raise ValidationError("Account number must be unique.")
        return account_number

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance is not None and balance < 0:
            raise ValidationError("Balance cannot be negative.")
        return balance
