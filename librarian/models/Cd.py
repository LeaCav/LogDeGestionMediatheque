from django.db import models
from .media import Media

class CD(Media):
    artist = models.CharField(max_length=255)