from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta
from loguru import logger

# Настройка логирования в файл
logger.add("setup_tasks.log", rotation="1 MB")

try:
    # Определение интервала (каждые 10 минут)
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.MINUTES,
    )
    logger.info("Интервал успешно создан или найден: каждые 10 минут")

    # Создание периодической задачи
    task = PeriodicTask.objects.create(
        interval=schedule,
        name='Fetch DEX Data',
        task='dex_transactions.tasks.fetch_dex_data',
    )
    logger.info(f"Периодическая задача '{task.name}' успешно создана")
except Exception as e:
    logger.error(f"Произошла ошибка при создании задачи: {e}")

