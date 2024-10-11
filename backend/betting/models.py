from django.db import models
from django.contrib.auth import get_user_model
from loguru import logger

# Инициализация логирования
logger.add("logs/bet_creation.log", rotation="10 MB")

class Bet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
    trend = models.CharField(max_length=10)  # 'up' или 'down'
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Логирование перед сохранением
        logger.info(f"Создание ставки: пользователь={self.user}, токен={self.token}, тренд={self.trend}, сумма={self.amount}")
        super().save(*args, **kwargs)
        # Логирование после сохранения
        logger.info(f"Ставка сохранена: ID={self.id}, время={self.created_at}")


