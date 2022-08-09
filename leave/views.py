from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Leave
from .forms import LeaveForm
from django.utils import timezone

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def currentleave(request) :
    leave = Leave.objects.filter(user= request.user)
    url = request.path
    return render(request, 'leave/currentleave.html', {
        "leave": leave,
        "time_now": timezone.now(),
        "url": url,
    })

@login_required
def leaveform(request) :
    if request.method == "GET":
        return render(request, 'leave/leaveform.html', {
            "form": LeaveForm()
        })
    else :
        try :
            form = LeaveForm(request.POST)
            newleave = form.save(commit=False)     # don't save it in the database
            newleave.user = request.user
            newleave.save()
            return redirect('leave:currentleave')
        except ValueError:
            return render(request, 'leave/leaveform.html', {
                'form': LeaveForm(),
                "error": form.errors
            })

@login_required
def viewleave(request, leave_pk):
    leave = get_object_or_404(Leave, pk=leave_pk, user=request.user)
    if request.method == "GET":
        form = LeaveForm(instance=leave)
        return render(request, 'leave/viewleave.html', {
            'leave': leave,
            "form": form,
            "time_now": timezone.now(),
        })
    else:
        try:
            form = LeaveForm(request.POST, instance=leave)
            form.save()
            return redirect('leave:currentleave')
        except ValueError:
            return render(request, 'leave/viewleave.html', {
               'leave': leave,
               "form": form,
               "error": form.errors
           })


@login_required
def deleteleave(request, leave_pk):
    leave = get_object_or_404(Leave, pk=leave_pk, user=request.user)
    if request.method == "POST":
        leave.delete()
        return redirect('leave:currentleave')