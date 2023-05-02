from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import Tweet, TweetLike, Comment
from .serializers import TweetSerializer, CommentSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [SessionAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
