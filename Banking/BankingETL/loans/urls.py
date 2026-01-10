from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_loan, name='apply_loan'),
    path('', views.loan_list, name='loan_list'),
    path('update/<int:pk>/', views.loan_update, name='loan_update'),
]
