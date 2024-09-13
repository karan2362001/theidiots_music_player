from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Emotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood}"
