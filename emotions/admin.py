from django.contrib import admin

# Register your models here.
from .models import Emotion

admin.site.register(Emotion)