from django.db import models
from django.contrib.auth import get_user_model

class Portfolio(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token_idea_balance = models.DecimalField(max_digits=20, decimal_places=8)
    token_matter_balance = models.DecimalField(max_digits=20, decimal_places=8)
    updated_at = models.DateTimeField(auto_now=True)

