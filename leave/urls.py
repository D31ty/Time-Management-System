from django.urls import path
from . import views

app_name = 'leave'

urlpatterns = [
    path('', views.currentleave, name="currentleave"),
    path('form/', views.leaveform, name="leaveform"),
    path('viewleave/<int:leave_pk>', views.viewleave, name="viewleave"),
    path('leavehistory/', views.currentleave, name="leavehistory"),
    path('leave/<int:leave_pk>/delete', views.deleteleave, name="deleteleave"),
]