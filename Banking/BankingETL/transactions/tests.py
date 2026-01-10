from django.test import TestCase, Client
from django.urls import reverse
from .models import Transaction
from accounts.models import Account
from customers.models import Customer
from branches.models import Branch

class TransactionViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test branch
        self.branch = Branch.objects.create(
            name='Main Branch',
            address='123 Main St',
            city='Anytown',
            contact_number='123-456-7890'
        )
        # Create test customers
        self.customer1 = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='1234567890',
            address='456 Elm St',
            branch=self.branch
        )
        self.customer2 = Customer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            phone='0987654321',
            address='789 Oak St',
            branch=self.branch
        )
        # Create test accounts
        self.account1 = Account.objects.create(
            account_number='123456789',
            customer=self.customer1,
            account_type='SAVINGS',
            balance=1000.00
        )
        self.account2 = Account.objects.create(
            account_number='987654321',
            customer=self.customer2,
            account_type='CHECKING',
            balance=500.00
        )

    def test_deposit_view(self):
        data = {
            'account': self.account1.id,
            'amount': 200.00,
            'description': 'Test deposit'
        }
        response = self.client.post(reverse('deposit'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.account1.refresh_from_db()
        self.assertEqual(self.account1.balance, 1200.00)
        self.assertTrue(Transaction.objects.filter(to_account=self.account1, transaction_type='DEPOSIT', amount=200.00).exists())

    def test_withdraw_view_success(self):
        data = {
            'account': self.account1.id,
            'amount': 100.00,
            'description': 'Test withdrawal'
        }
        response = self.client.post(reverse('withdraw'), data)
        self.assertEqual(response.status_code, 302)
        self.account1.refresh_from_db()
        self.assertEqual(self.account1.balance, 900.00)
        self.assertTrue(Transaction.objects.filter(from_account=self.account1, transaction_type='WITHDRAWAL', amount=100.00).exists())

    def test_withdraw_view_insufficient_balance(self):
        data = {
            'account': self.account1.id,
            'amount': 1500.00,
            'description': 'Test withdrawal'
        }
        response = self.client.post(reverse('withdraw'), data)
        self.assertEqual(response.status_code, 200)  # Stay on page with error
        self.account1.refresh_from_db()
        self.assertEqual(self.account1.balance, 1000.00)  # Balance unchanged
        self.assertFalse(Transaction.objects.filter(amount=1500.00).exists())

    def test_transfer_view_success(self):
        data = {
            'from_account': self.account1.id,
            'to_account': self.account2.id,
            'amount': 300.00,
            'description': 'Test transfer'
        }
        response = self.client.post(reverse('transfer'), data)
        self.assertEqual(response.status_code, 302)
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 700.00)
        self.assertEqual(self.account2.balance, 800.00)
        self.assertTrue(Transaction.objects.filter(from_account=self.account1, to_account=self.account2, transaction_type='TRANSFER', amount=-300.00).exists())
        self.assertTrue(Transaction.objects.filter(from_account=self.account2, to_account=self.account1, transaction_type='TRANSFER', amount=300.00).exists())

    def test_transfer_view_same_account(self):
        data = {
            'from_account': self.account1.id,
            'to_account': self.account1.id,
            'amount': 100.00,
            'description': 'Test transfer'
        }
        response = self.client.post(reverse('transfer'), data)
        self.assertEqual(response.status_code, 200)  # Stay on page with error
        self.account1.refresh_from_db()
        self.assertEqual(self.account1.balance, 1000.00)  # Balance unchanged

    def test_transaction_list(self):
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response.status_code, 200)
        # Assuming some transactions exist, but in test DB they might not
