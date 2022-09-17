from django.urls import path
from event.api import views

urlpatterns = [
    path("list-event",views.EventListApiView.as_view())
]
