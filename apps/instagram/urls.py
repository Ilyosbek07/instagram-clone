from django.urls import path

from apps.instagram.views import (
    ProfileRetrieveAPIView,
    StoryListAPIView,
    PostListAPIView, CommentListAPIView,

)

urlpatterns = [
    path('profile/<int:pk>/', ProfileRetrieveAPIView.as_view(), name='profile-detail'),
    path('post/', PostListAPIView.as_view(), name='post'),
    path('post/<int:pk>/comments/', CommentListAPIView.as_view(), name='comment'),
    path('story/', StoryListAPIView.as_view(), name='story'),
]
