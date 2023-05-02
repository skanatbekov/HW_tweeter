from django.db import models
from accounts.models import User


class Tweet(models.Model):
    title = models.CharField(max_length=240)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tweets')

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    tweet = models.ForeignKey(Tweet, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')

    def __str__(self):
        return self.body


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    is_like = models.BooleanField()

    class Meta:
        unique_together = ['user', 'tweet']

    def __str__(self):
        return f'{self.user} - {self.tweet}: {self.is_like}'


