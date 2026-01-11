from django import forms
from .models import Customer
from branches.models import Branch

class CustomerForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'branch']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter full address', 'rows': 3}),
        }
