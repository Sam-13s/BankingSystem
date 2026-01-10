from django import forms
from django.core.exceptions import ValidationError
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['customer', 'loan_type', 'amount', 'tenure_months', 'emi_amount', 'linked_account']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'tenure_months': forms.NumberInput(attrs={'class': 'form-control'}),
            'emi_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'linked_account': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError("Loan amount must be positive.")
        return amount

    def clean_tenure_months(self):
        tenure = self.cleaned_data.get('tenure_months')
        if tenure is not None and tenure <= 0:
            raise ValidationError("Tenure must be positive.")
        return tenure

    def clean_emi_amount(self):
        emi = self.cleaned_data.get('emi_amount')
        if emi is not None and emi <= 0:
            raise ValidationError("EMI amount must be positive.")
        return emi
