from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your models here.
class BroadcastNotification(models.Model):
    messgae = models.TextField()
    broadcast_on = models.DateTimeField()
    interval = models.TimeField()
    sent = models.BooleanField(default=False)
    class meta:
        ordering = ['-broadcast_on']

@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(hour = instance.broadcast_on.hour, minute = instance.broadcst_on.minute)
        task = PeriodicTask.objects.create(crontab=schedule, name="broadcast_notification-"+str(instance.id), task = "notificatios_app.tasks.broadcast_notification", args=json.dumps((instance.id,)))
