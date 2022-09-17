from django.db import models


# class CommentModel(models.Model):
    # pass


class EventPhotoModel(models.Model):
    event_id = models.ForeignKey("event.EventModel",on_delete=models.CASCADE,null=False,blank=False)
    image = models.ImageField(upload_to="event_photos/",null=False,blank=False)

    def __str__(self):
        return f"Photo of {self.event_id.name} event"


class OrganizerModel(models.Model):
    user = models.ForeignKey("user.CustomUserModel",on_delete=models.CASCADE,null=False,blank=False)
    first_name = models.CharField(max_length=200, null=False,blank=False)
    last_name = models.CharField(max_length=200, null=False,blank=False)
    phonenumber = models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EventPlaceModel(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    address = models.CharField(max_length=300,null=False,blank=False)
    # map_coordinate

    def __str__(self):
        return self.name

class EventModel(models.Model):
    organizer_id = models.ForeignKey("event.OrganizerModel",null=True,blank=False,on_delete=models.SET_NULL)
    event_place_id = models.ForeignKey("event.EventPlaceModel",null=True,blank=False,on_delete=models.SET_NULL)
    people_at_this_event = models.ManyToManyField("event.ParticipantModel")
    name = models.CharField(max_length=300,null=False,blank=False)
    entering_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_entering_price = models.BooleanField(default=False)
    starting_time = models.DateTimeField()
    # rating
    cover_image = models.ImageField(upload_to="event_images/",null=False,blank=False)


class InterestsModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ParticipantModel(models.Model):
    GENDER_CHOICES = [
        ("M","Male"),
        ("F","Female"),
    ]

    user = models.ForeignKey("user.CustomUserModel",on_delete=models.CASCADE,null=False,blank=False)
    interests = models.ManyToManyField("event.InterestsModel")
    first_name = models.CharField(max_length=70,null=False,blank=False)
    last_name = models.CharField(max_length=70,null=False,blank=False)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"