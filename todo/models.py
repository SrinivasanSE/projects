from django.db import models
from django.utils import timezone
# Create your models here.
class todo(models.Model):
    content = models.TextField()
    name=models.TextField(default='seenu')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
