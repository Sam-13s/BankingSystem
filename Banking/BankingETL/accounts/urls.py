from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),
    path('update/<int:pk>/', views.account_update, name='account_update'),
    path('delete/<int:pk>/', views.account_delete, name='account_delete'),
]