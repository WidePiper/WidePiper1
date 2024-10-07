from django.db import models
from django.contrib.auth import get_user_model

class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token_type = models.CharField(max_length=10)  # Например, 'idea' или 'matter'
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    transaction_type = models.CharField(max_length=50)  # Депозит или вывод
    timestamp = models.DateTimeField(auto_now_add=True)

