from django.db import models

from base.models import TodoList
class TodoList(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)