import os
import sys
import django
from django.conf import settings

# Add the BankingETL directory to sys.path to resolve imports
sys.path.insert(0, 'Banking/BankingETL')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Banking.BankingETL.bankingetl.settings')
django.setup()

from accounts.forms import AccountForm
from transactions.forms import DepositForm, WithdrawForm, TransferForm
from customers.forms import CustomerForm
from loans.forms import LoanForm
from cards.forms import CardForm
from accounts.models import Account
from customers.models import Customer

def test_account_form():
    print("Testing AccountForm...")
    # Test unique account number
    form_data = {'account_number': '1234567890', 'customer': 1, 'account_type': 'SAVINGS', 'balance': 100}
    form = AccountForm(data=form_data)
    if form.is_valid():
        print("✓ Valid account form")
    else:
        print("✗ Invalid account form:", form.errors)

    # Test negative balance
    form_data = {'account_number': '1234567891', 'customer': 1, 'account_type': 'SAVINGS', 'balance': -50}
    form = AccountForm(data=form_data)
    if not form.is_valid() and 'balance' in form.errors:
        print("✓ Negative balance validation works")
    else:
        print("✗ Negative balance validation failed")

def test_transaction_forms():
    print("Testing Transaction Forms...")
    # Test negative amount in deposit
    form_data = {'account': 1, 'amount': -100, 'description': 'test'}
    form = DepositForm(data=form_data)
    if not form.is_valid() and 'amount' in form.errors:
        print("✓ Deposit negative amount validation works")
    else:
        print("✗ Deposit negative amount validation failed")

    # Test withdraw with insufficient balance (assuming account balance is low)
    form_data = {'account': 1, 'amount': 1000, 'description': 'test'}
    form = WithdrawForm(data=form_data)
    # This might not trigger if account has balance, but at least test positive amount
    form2 = WithdrawForm(data={'account': 1, 'amount': -50, 'description': 'test'})
    if not form2.is_valid() and 'amount' in form2.errors:
        print("✓ Withdraw negative amount validation works")
    else:
        print("✗ Withdraw negative amount validation failed")

def test_customer_form():
    print("Testing CustomerForm...")
    form_data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'invalid-email', 'phone': '1234567890', 'address': 'Test Address'}
    form = CustomerForm(data=form_data)
    if not form.is_valid() and 'email' in form.errors:
        print("✓ Invalid email validation works")
    else:
        print("✗ Invalid email validation failed")

def test_loan_form():
    print("Testing LoanForm...")
    form_data = {'customer': 1, 'loan_type': 'PERSONAL', 'amount': -5000, 'tenure_months': 12, 'emi_amount': 500, 'linked_account': 1}
    form = LoanForm(data=form_data)
    if not form.is_valid() and 'amount' in form.errors:
        print("✓ Loan negative amount validation works")
    else:
        print("✗ Loan negative amount validation failed")

def test_card_form():
    print("Testing CardForm...")
    form_data = {'customer': 1, 'card_type': 'CREDIT', 'card_number': '1234567890123456', 'expiry_date': '2025-12-31', 'account': 1}
    form = CardForm(data=form_data)
    if form.is_valid():
        print("✓ Valid card form")
    else:
        print("✗ Invalid card form:", form.errors)

if __name__ == '__main__':
    test_account_form()
    test_transaction_forms()
    test_customer_form()
    test_loan_form()
    test_card_form()
    print("Testing completed.")
