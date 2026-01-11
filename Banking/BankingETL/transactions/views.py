from django.shortcuts import render, redirect
from .forms import DepositForm, WithdrawForm, TransferForm
from .models import Transaction
from accounts.models import Account
from django.contrib import messages

def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data.get('description', '')
            account.balance += amount
            account.save()
            Transaction.objects.create(from_account=None, to_account=account, transaction_type='DEPOSIT', amount=amount, description=description)
            messages.success(request, 'Deposit successful.')
            return redirect('deposit')
    else:
        form = DepositForm()
    return render(request, 'transactions/deposit.html', {'form': form})

def withdraw_view(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data.get('description', '')
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(from_account=account, to_account=None, transaction_type='WITHDRAW', amount=amount, description=description)
                messages.success(request, 'Withdrawal successful.')
                return redirect('withdraw')
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = WithdrawForm()
    return render(request, 'transactions/withdraw.html', {'form': form})

def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = form.cleaned_data['from_account']
            to_account = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data.get('description', '')
            if from_account != to_account and from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()
                Transaction.objects.create(from_account=from_account, to_account=to_account, transaction_type='TRANSFER', amount=amount, description=description)
                messages.success(request, 'Transfer successful.')
                return redirect('transfer')
            else:
                messages.error(request, 'Invalid transfer.')
    else:
        form = TransferForm()
    return render(request, 'transactions/transfer.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})
