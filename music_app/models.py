from django.db import models

# Create your models here.
# [時間、曲名、アーティスト名、Switch]

class SpotifyAlarmModel(models.Model):
    time = models.TimeField()
    track_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    switch = models.BooleanField()

    def __str__(self):
        return self.track_name
