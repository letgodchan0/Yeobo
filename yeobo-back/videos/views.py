from django.shortcuts import render
from .models import Video, Comment
from .serializers.video import VideoSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
@api_view(['GET'])
def video_list(request):
    videos = get_list_or_404(Video)
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def video_detail(request, video_pk):
    video = get_object_or_404(Video, pk=video_pk)
    serializer = VideoSerializer(video)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, video_pk):
    user = request.user
    video = get_object_or_404(Video, pk=video_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(video=video, user=user)
        
        comments = video.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, video_pk, comment_pk):
    video = get_object_or_404(Video, pk=video_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = video.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = video.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()