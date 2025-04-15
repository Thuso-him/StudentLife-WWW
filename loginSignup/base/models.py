from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, default="")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today)


    def __str__(self):
        return self.title
