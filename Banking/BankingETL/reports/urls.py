from django.urls import path
from . import views

urlpatterns = [
    path('upload-csv/', views.upload_customers_csv, name='upload_csv'),
    path('customer-report/', views.customer_report, name='customer_report'),
    path('customer-report/download/', views.download_customer_report_csv, name='download_customer_report_csv'),
     path('customer-report/download/excel/', views.download_customer_report_excel, name='download_customer_report_excel'),
    path('customer-chart-data/', views.customer_chart_data, name='customer_chart_data'),
    path('transaction-report/', views.transaction_report, name='transaction_report'),
    path('transaction-chart-data/', views.transaction_chart_data, name='transaction_chart_data'),
]
