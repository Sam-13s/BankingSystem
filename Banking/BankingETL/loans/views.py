

from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoanForm
from .models import Loan
from django.contrib import messages

def apply_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Loan application submitted successfully.')
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'loans/apply_loan.html', {'form': form})

def loan_list(request):
    loans = Loan.objects.select_related('customer', 'linked_account').all()
    return render(request, 'loans/loan_list.html', {'loans': loans})

def loan_update(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Loan updated successfully.')
            return redirect('loan_list')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'loans/loan_form.html', {'form': form, 'loan': loan})
