from django.db import models
from .media import Media

class DVD(Media):
    director = models.CharField(max_length=255)