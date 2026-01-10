from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from customers.models import Customer
from transactions.models import Transaction
import csv
from django.contrib import messages
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from django.db.models import Count
from django.utils import timezone
import datetime

def upload_customers_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            Customer.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                phone=row['phone'],
                address=row['address']
            )
        messages.success(request, 'Customers uploaded successfully.')
    return render(request, 'reports/upload_csv.html')

def customer_report(request):
    customers = Customer.objects.all()
    return render(request, 'reports/customer_report.html', {'customers': customers})

def download_customer_report_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer_report.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'Address'])
    for customer in Customer.objects.all():
        writer.writerow([customer.first_name, customer.last_name, customer.email, customer.phone, customer.address])
    return response

def download_customer_report_excel(request):
    # For simplicity, using CSV as Excel
    return download_customer_report_csv(request)

def customer_chart_data(request):
    customers = Customer.objects.all()
    labels = []
    data = []
    for customer in customers:
        labels.append(f"{customer.first_name} {customer.last_name}")
        total_balance = sum(account.balance for account in customer.accounts.all())
        data.append(float(total_balance))
    return JsonResponse({'labels': labels, 'data': data})

def transaction_report(request):
    return render(request, 'reports/transaction_report.html')

def transaction_chart_data(request):
    # Get transactions from last 30 days
    end_date = timezone.now()
    start_date = end_date - datetime.timedelta(days=30)
    transactions = Transaction.objects.filter(timestamp__range=(start_date, end_date)).order_by('timestamp')

    # Group by date
    data = {}
    for transaction in transactions:
        date = transaction.timestamp.date().isoformat()
        if date not in data:
            data[date] = 0
        data[date] += float(transaction.amount)

    labels = sorted(data.keys())
    values = [data[date] for date in labels]
    return JsonResponse({'labels': labels, 'data': values})
