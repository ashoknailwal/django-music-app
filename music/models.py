from django.db import models
from django.contrib.auth.models import Permission , User

# Create your models here.
class Album(models.Model):
    user = models.ForeignKey(User,default='1')
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title
