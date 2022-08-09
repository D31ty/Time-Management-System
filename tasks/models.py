from django.db import models
from django.utils import timezone

from register.models import UserAccount
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title