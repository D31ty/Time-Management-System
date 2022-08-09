from django.db import models
from django.utils import timezone

from register.models import UserAccount

# Create your models here.
class Meeting(models.Model):
    purpose = models.CharField(max_length=250, blank = False,)
    venue = models.CharField(max_length=100, blank = False,)
    meet_date = models.DateField(blank = False,)
    from_time = models.TimeField(blank = False,)
    to_time = models.TimeField(blank = False,)
    important = models.BooleanField(default=False)
    dateassigned = models.DateTimeField(default=timezone.now)
    meet_link = models.URLField()
    attended = models.BooleanField(default=False)
    members = models.ManyToManyField(UserAccount, blank = False, related_name = "meeting_members")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.purpose
