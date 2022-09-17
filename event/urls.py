from django.urls import path, include

app_name = "event"

urlpatterns = [
    path("api/", include("event.api.urls"))
]
