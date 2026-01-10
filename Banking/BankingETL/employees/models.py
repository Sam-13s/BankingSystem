from django.db import models

class Employee(models.Model):
    EMPLOYEE_ROLES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=EMPLOYEE_ROLES)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

