from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
