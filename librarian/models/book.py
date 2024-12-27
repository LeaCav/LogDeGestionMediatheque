from django.db import models
from .media import Media

class Book(Media):
    author = models.CharField(max_length=255)