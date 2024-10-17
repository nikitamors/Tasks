from celery import shared_task
from .models import Task
from datetime import datetime


@shared_task
def send_task_deadline_notifications():
    now = datetime.now()
    tasks = Task.objects.filter(due_date__lte=now, completed=False)
    for task in tasks:
        # Логика отправки уведомлений
        print(f"Отправлено уведомление для задачи: {task.title}")
