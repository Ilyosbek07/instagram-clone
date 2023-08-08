from django.urls import path

from apps.instagram.views import (
    ProfileRetrieveAPIView,
    ProfileDestroyAPIView,
    PostDestroyAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostListAPIView,
    PostCommentListAPIView,
    StoryListAPIView,
    StoryCreateAPIView,
    StoryRetrieveAPIView,
    StoryDestroyAPIView,
    StoryCommentListAPIView
)

urlpatterns = [
    # PROFILE endpoinsts
    path('profile/<int:pk>/', ProfileRetrieveAPIView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/', ProfileDestroyAPIView.as_view(), name='profile-delete'),

    # POSTS endpoinsts
    path('post/', PostListAPIView.as_view(), name='post'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/<int:pk>/detail/', PostRetrieveAPIView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDestroyAPIView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/', PostCommentListAPIView.as_view(), name='post-comments'),

    # STORY endpoinsts
    path('story/', StoryListAPIView.as_view(), name='story'),
    path('post/create/', StoryCreateAPIView.as_view(), name='story-create'),
    path('post/<int:pk>/detail/', StoryRetrieveAPIView.as_view(), name='story-detail'),
    path('post/<int:pk>/delete/', StoryDestroyAPIView.as_view(), name='story-delete'),
    path('post/<int:pk>/comments/', StoryCommentListAPIView.as_view(), name='story-comments'),

]
