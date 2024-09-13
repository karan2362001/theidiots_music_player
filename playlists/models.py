from django.db import models
from django.contrib.auth import get_user_model
from music.models import Song

User = get_user_model()

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return f"{self.name} - {self.user.username}"
