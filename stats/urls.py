#My coding
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'stats'
urlpatterns = [
    path('', views.stats, name="stats"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)