from rest_framework import serializers
from event import models


class EventModelSerializer(serializers.ModelSerializer):
    event_place_name = serializers.CharField(source="event_place_id.name")
    event_place_address = serializers.CharField(source="event_place_id.address")
    class Meta:
        model = models.EventModel
        # fields = ("organizer_id","event_place_name","event_place_address","name","entering_price","is_entering_price","starting_time","cover_image","people_at_this_event")
        fields = "__all__"
        # exclude = ["event_place_id"]
        