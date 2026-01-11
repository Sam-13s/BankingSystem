"""
URL configuration for bankingetl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('customers/', include('customers.urls')),  # Customers app
    path('accounts/', include('accounts.urls')), # Accounts
    path('transactions/', include('transactions.urls')),
    path('branches/', include('branches.urls')),
    path('cards/', include('cards.urls')),
    path('employees/', include('employees.urls')),
    path('reports/', include('reports.urls')),  # Reports & ETL Logs
    path('dashboard/', include('dashboard.urls')),
    path('', include('dashboard.urls')),  # Default to dashboard
]
