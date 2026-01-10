from django.test import TestCase, Client
from django.urls import reverse
from .models import Account
from customers.models import Customer
from branches.models import Branch

class AccountViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test branch
        self.branch = Branch.objects.create(
            name='Main Branch',
            address='123 Main St',
            city='Anytown',
            contact_number='123-456-7890'
        )
        # Create a test customer
        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='1234567890',
            address='456 Elm St',
            branch=self.branch
        )
        # Create a test account
        self.account = Account.objects.create(
            account_number='123456789',
            customer=self.customer,
            account_type='SAVINGS',
            balance=1000.00
        )

    def test_account_list(self):
        response = self.client.get(reverse('account_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.account_number)

    def test_account_create(self):
        data = {
            'account_number': '987654321',
            'customer': self.customer.id,
            'account_type': 'CHECKING',
            'balance': 500.00
        }
        response = self.client.post(reverse('account_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Account.objects.filter(account_number='987654321').exists())

    def test_account_update(self):
        data = {
            'account_number': '123456789',
            'customer': self.customer.id,
            'account_type': 'SAVINGS',
            'balance': 1500.00
        }
        response = self.client.post(reverse('account_update', args=[self.account.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 1500.00)

    def test_account_delete(self):
        response = self.client.post(reverse('account_delete', args=[self.account.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Account.objects.filter(pk=self.account.pk).exists())
