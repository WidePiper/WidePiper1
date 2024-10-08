from django.db import models

class DexTransaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    token_pair = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    volume = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.token_pair} at {self.timestamp}"


