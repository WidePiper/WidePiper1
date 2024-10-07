from django.db import models
from django.contrib.auth import get_user_model

class Bet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
    trend = models.CharField(max_length=10)  # 'up' или 'down'
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

