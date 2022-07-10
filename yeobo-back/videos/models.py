from statistics import mode
from django.db import models
from django.conf import settings
# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

class Video(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='videos')
    published_at = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.TextField()
    channel_title = models.CharField(max_length=300)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
