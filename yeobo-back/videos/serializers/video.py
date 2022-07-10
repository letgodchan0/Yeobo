from msilib.schema import MoveFile
from rest_framework import serializers
from .comment import CommentSerializer
from ..models import Video
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ('pk', 'city', 'published_at', 'title', 'description', 'url', 'channel_title', 'comments')