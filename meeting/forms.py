from django import forms
from django.forms import ModelForm
from django.utils import timezone
from .models import Meeting
from datetime import datetime
from register.models import UserAccount

from django.core.exceptions import ValidationError


def validate_meetdate(value):
    if value < datetime.now().date():
        raise ValidationError((f"{value} is invalid date."),params = {'value':value})

def validate_time(value):
    if value < datetime.now().time():
        raise ValidationError((f"{value} is invalid time."),params = {'value': value})

class MeetingForm(ModelForm):
    meet_date = forms.DateField(validators = [validate_meetdate])
    members = forms.ModelMultipleChoiceField(queryset=UserAccount.objects.all(), widget=forms.CheckboxSelectMultiple())
    from_time = forms.TimeField(validators = [validate_time])
    to_time = forms.TimeField(validators = [validate_time])
    class Meta:
        model = Meeting 
        fields = ["purpose", "meet_date", "from_time", "to_time", "venue", "members", "meet_link", "important"]

