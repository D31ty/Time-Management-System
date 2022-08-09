from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import MeetingForm
from .models import Meeting
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Meeting
from register.models import UserAccount
# Create your views here.

@login_required
def currentmeetings(request):
    url = request.path
    #meetings = Meeting.objects.all()
    meetings = Meeting.objects.filter(members=request.user)
    #print(f"{request.user.id} is the request user of the page")
    return render(request, 'meeting/currentmeeting.html', {
        "meetings": meetings,
        "date_now": datetime.now().date(),
        "time_now": datetime.now().time(),
        "url": url,
    })
    return render(request, 'meeting/currentmeeting.html')


@login_required
def meetingform(request):
    members = UserAccount.objects.all()
    host = request.user
    if request.method == "GET":
        return render(request, 'meeting/meetingform.html', {
            "form": MeetingForm(),
            "users": members,
            "host": host
        })
    else :
        try :
            form = MeetingForm(request.POST)
            newmeet = form.save(commit=False)     # don't save it in the database
            newmeet.user = request.user
            newmeet.save()
            return redirect('meeting:currentmeetings')
        except ValueError:
            return render(request, 'meeting/meetingform.html', {
                'form': MeetingForm(),
                "users": members,
                "host": host,
                "error": form.errors
            })



@login_required
def viewmeeting(request, meeting_pk):
    meeting = get_object_or_404(Meeting, pk=meeting_pk)
    if request.method == "GET":
        form = MeetingForm(instance=meeting)
        return render(request, 'meeting/viewmeeting.html', {
            'meeting': meeting,
            "form": form,
            "date_now": datetime.now().date(),
            "time_now": datetime.now().time(),
        })
    else:
        try:
            form = MeetingForm(request.POST, instance=meeting)
            form.save()
            return redirect('meeting:currentmeetings')
        except ValueError:
            return render(request, 'meeting/viewmeeting.html', {
               'meeting': meeting,
               "form": form,
               "error": form.errors
           })

@login_required
def deletemeeting(request, meeting_pk):
    meeting = get_object_or_404(Meeting, pk=meeting_pk, user=request.user)
    if request.method == "POST":
        meeting.delete()
        return redirect('meeting:currentmeetings')


@login_required
def attended(request, meeting_pk):
    meetings = Meeting.objects.filter(user=request.user)
    meet = meetings.get(pk=meeting_pk)
    if request.method == "POST":
        meet.attended = True
        meet.save()
        return redirect('meeting:currentmeetings')
