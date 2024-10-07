from django.db import models

class BlockchainTransaction(models.Model):
    transaction_hash = models.CharField(max_length=256)
    token = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=50)  # Например, 'pending', 'completed'
    created_at = models.DateTimeField(auto_now_add=True)

