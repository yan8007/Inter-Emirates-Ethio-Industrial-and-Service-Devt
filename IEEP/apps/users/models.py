from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('MANAGER', 'Production Manager'),
        ('ENGINEER', 'Maintenance Engineer'),
        ('INVENTORY', 'Inventory Clerk'),
        ('PROCUREMENT', 'Procurement Specialist'),
        ('FINANCE', 'Finance Officer'),
        ('VIEWER', 'Read-Only User')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='VIEWER')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
