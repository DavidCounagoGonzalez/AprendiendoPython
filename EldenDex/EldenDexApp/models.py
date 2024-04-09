from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Creatures(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    image = models.CharField(blank=True, default='')
    description = models.TextField()
    location = models.CharField(blank=True)
    drops = ArrayField(models.CharField(blank=True, default=''))