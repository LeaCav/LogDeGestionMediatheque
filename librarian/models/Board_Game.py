from django.db import models

class BoardGame(models.Model):
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)