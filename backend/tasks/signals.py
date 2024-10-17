from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import send_task_deadline_notifications


@receiver(post_save, sender=Task)
def task_saved_handler(sender, instance, created, **kwargs):
    if created:
        send_task_deadline_notifications.delay()
