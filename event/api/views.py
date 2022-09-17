from rest_framework import generics
from event import models
from event.api import serializers 


class EventListApiView(generics.ListAPIView):
    queryset = models.EventModel.objects.all()
    serializer_class = serializers.EventModelSerializer