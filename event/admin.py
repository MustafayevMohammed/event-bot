from django.contrib import admin
from event.models import EventPhotoModel, OrganizerModel, EventPlaceModel, EventModel, InterestsModel, ParticipantModel

# Register your models here.

admin.site.register(EventPhotoModel)
admin.site.register(OrganizerModel)
admin.site.register(EventPlaceModel)
admin.site.register(EventModel)
admin.site.register(InterestsModel)
admin.site.register(ParticipantModel)