from django.urls import path
from . import views

urlpatterns = [
    
    path('deposit/', views.deposit_view, name='deposit'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('transfer/', views.transfer_view, name='transfer'),
    path('', views.transaction_list, name='transaction_list')
]
