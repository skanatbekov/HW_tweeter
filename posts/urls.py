from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('comment', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
