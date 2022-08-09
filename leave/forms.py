#My coding

from django import forms
from django.forms import ModelForm

from .models import Leave
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone

def validate_todate(value):
    if value < timezone.now():
        raise ValidationError((f"{value} is invalid date."),params = {'value':value})

class LeaveForm(ModelForm):
    to_date = forms.DateTimeField(validators=[validate_todate])
    class Meta:
        model = Leave 
        fields = ["from_date", "to_date", "title", "memo", "important",]

