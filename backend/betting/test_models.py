import os
import django
from django.test import TestCase
from django.contrib.auth import get_user_model
from loguru import logger
from .models import Bet

# Настраиваем Django перед запуском тестов
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Проверьте, что 'backend.settings' — правильный путь к файлу настроек
django.setup()

# Инициализация логирования
logger.add("logs/bet_creation.log", rotation="10 MB")

class BetModelTest(TestCase):

    def setUp(self):
        # Создаём тестового пользователя
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123'
        )

    def test_create_bet(self):
        # Проверяем, что создаётся ставка и сохраняются все данные корректно
        bet = Bet.objects.create(
            user=self.user,
            token='BTC/USDT',
            trend='up',
            amount=1000.00
        )
        self.assertEqual(bet.user, self.user)
        self.assertEqual(bet.token, 'BTC/USDT')
        self.assertEqual(bet.trend, 'up')
        self.assertEqual(bet.amount, 1000.00)
        self.assertIsNotNone(bet.created_at)

    def test_logging(self):
        # Удаляем старый лог-файл, если он существует
        log_file_path = "logs/bet_creation.log"
        if os.path.exists(log_file_path):
            os.remove(log_file_path)

        # Создаём ставку
        Bet.objects.create(
            user=self.user,
            token='BTC/USDT',
            trend='up',
            amount=1500.00
        )

        # Проверяем, что лог-файл создан и содержит записи
        self.assertTrue(os.path.exists(log_file_path))
        with open(log_file_path, 'r') as f:
            log_content = f.read()
            self.assertIn('Создание ставки', log_content)
            self.assertIn('Ставка сохранена', log_content)
