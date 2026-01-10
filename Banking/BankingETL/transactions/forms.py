

from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction
from accounts.models import Account

class DepositForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be positive.")
        return amount

class WithdrawForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be positive.")
        return amount

    def clean(self):
        cleaned_data = super().clean()
        account = cleaned_data.get('account')
        amount = cleaned_data.get('amount')
        if account and amount and account.balance < amount:
            raise ValidationError("Insufficient balance for withdrawal.")
        return cleaned_data

class TransferForm(forms.Form):
    from_account = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    to_account = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be positive.")
        return amount

    def clean(self):
        cleaned_data = super().clean()
        from_account = cleaned_data.get('from_account')
        to_account = cleaned_data.get('to_account')
        amount = cleaned_data.get('amount')
        if from_account and to_account and amount:
            if from_account == to_account:
                raise ValidationError("From and to accounts cannot be the same.")
            if from_account.balance < amount:
                raise ValidationError("Insufficient balance for transfer.")
        return cleaned_data
