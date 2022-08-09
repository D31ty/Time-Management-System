from django.db import models
from django.utils import timezone

from register.models import UserAccount
# Create your models here.
class Leave(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField(blank=False)
    from_date = models.DateTimeField(blank = False, auto_now=False, auto_now_add=False)
    datesubmitted = models.DateTimeField(default=timezone.now)
    to_date = models.DateTimeField(blank=False, auto_now=False, auto_now_add=False)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title