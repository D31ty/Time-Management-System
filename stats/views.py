from django.shortcuts import render, redirect, get_object_or_404
from register.models import UserAccount
from meeting.models import Meeting
from django.contrib.auth.decorators import login_required

from datetime import datetime
#from matplotlib import pyplot as plt
#import numpy as np

# Create your views here.
@login_required
def stats(request):
    meetings = Meeting.objects.filter(members=request.user)
    count = 0
    attended_count = 0
    duration = 0

    for meeting in meetings:
        count += 1
        if meeting.attended == True:
            attended_count += 1  

        FMT = '%H:%M:%S'
        difference = datetime.strptime(str(meeting.to_time), FMT) - datetime.strptime(str(meeting.from_time), FMT)
        duration = difference
              

    #y = np.array([attended_count, (count - attended_count)])
    #labels = ["Attended", "Missed Meetings"]
    #plot = plt.pie(y, labels = labels)
    #plt.show()
    #plt.savefig('static/stats/piechart.jpg')

    return render(request, 'stats/statistics.html', {
        "meetings": meetings,
        "count": count,
        "attended": attended_count,
        "duration": duration,
    })

