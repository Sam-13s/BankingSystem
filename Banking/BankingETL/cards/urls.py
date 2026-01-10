from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('create/', views.card_create, name='card_create'),
    path('update/<int:pk>/', views.card_update, name='card_update'),
    path('delete/<int:pk>/', views.card_delete, name='card_delete'),
    path('issue/', views.issue_card, name='issue_card'),
    path('block/<int:pk>/', views.block_card, name='block_card'),
    path('renew/<int:pk>/', views.renew_card, name='renew_card'),
]
