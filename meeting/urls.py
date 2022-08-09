from django.urls import path
from . import views

app_name = 'meeting'
urlpatterns = [
    path('', views.currentmeetings, name="currentmeetings"),
    path('meetingform/', views.meetingform, name="meetingform"),
    path('meeting/<int:meeting_pk>/', views.viewmeeting, name="viewmeeting"),
    path('meetinghistory/', views.currentmeetings, name="meetinghistory"),
    path('meeting/<int:meeting_pk>/delete', views.deletemeeting, name="deletemeeting"),
     path('attended/<int:meeting_pk>', views.attended, name="attended"),
]