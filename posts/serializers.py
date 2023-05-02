from rest_framework import serializers

from .models import Tweet, TweetLike, Comment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['user', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', ]
