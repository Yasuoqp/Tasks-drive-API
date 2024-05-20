from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    date = models.DateTimeField(auto_now=True)
    urgency = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    update_data = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=15, blank=True)
    route = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=100, blank=True)
    driver = models.CharField(max_length=150, blank=True)
    product = models.CharField(max_length=150, blank=True)
    deadline = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=350, blank=True)
    delivery_status = models.CharField(max_length=150, blank=True)
    owner = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
