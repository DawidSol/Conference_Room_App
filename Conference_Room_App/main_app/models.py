from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_available = models.BooleanField()


class Reservation(models.Model):
    date = models.DateField(unique=True)
    comment = models.TextField(null=True, blank=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class Meta(models.Model):
    unique_together = ('date', 'room_id')
