from celery import shared_task
from .models import DexTransaction
import requests
from loguru import logger

# Настройка логирования в файл
logger.add("tasks.log", rotation="1 MB")

@shared_task
def fetch_dex_data():
    logger.info("Запуск задачи fetch_dex_data")
    try:
        response = requests.get("https://api.dex.example.com/price")
        response.raise_for_status()  # Проверяем статус ответа
        data = response.json()
        logger.info("Данные успешно получены с API")

        # Создание записи о транзакции
        DexTransaction.objects.create(
            token_pair=data['pair'],
            price=data['price'],
            volume=data['volume']
        )
        logger.info(f"Транзакция для пары {data['pair']} успешно создана")

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе к API: {e}")
    except Exception as e:
        logger.error(f"Произошла ошибка при обработке данных: {e}")
