from django.db import models
from django.contrib.auth import get_user_model
from music.models import Song

User = get_user_model()

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)  # e.g., "Recommended based on your mood"
    recommended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.song.title} recommended"
