from django.db import models

# Create your models here.

class EventPhotoModel(models.Model):
    event_id = models.ForeignKey("event.EventModel",on_delete=models.CASCADE,null=False,blank=False)
    image = models.ImageField(upload_to="event_photos/",null=False,blank=False)


class OrganizerModel(models.Model):
    # user
    first_name = models.CharField(max_length=200, null=False,blank=False)
    last_name = models.CharField(max_length=200, null=False,blank=False)
    # phonenumber

class EventModel(models.Model):
    # organizer_id
    # event_place_id
    # people_at_this_event
    pass