from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(100)
    description = models.TextField(100)
    is_completed = models.BooleanField(default=False)
