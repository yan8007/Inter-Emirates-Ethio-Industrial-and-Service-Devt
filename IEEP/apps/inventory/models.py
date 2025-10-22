from django.db import models
from apps.products.models import Product
from apps.users.models import CustomUser

class InventoryTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('PURCHASE', 'Purchase'),
        ('SALE', 'Sale'),
        ('PRODUCTION', 'Production'),
        ('ADJUSTMENT', 'Stock Adjustment'),
        ('TRANSFER', 'Warehouse Transfer')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Update product stock based on transaction
        if self.transaction_type in ['PURCHASE', 'PRODUCTION']:
            self.product.current_stock += self.quantity
        elif self.transaction_type in ['SALE']:
            self.product.current_stock -= self.quantity
        
        self.product.save()
        super().save(*args, **kwargs)

