from django.shortcuts import render
from rest_framework import generics

from apps.instagram.models import Profile, Post, Story, Comment
from apps.instagram.serializers import ProfileSerializer, PostSerializer, StorySerializer, CommentSerializer


# API for Profile

class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




class ProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# API for Posts

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        context = {
            'message': 'Hello, Django!',
        }
        return render(request, 'home.html', context)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# API for Stories
class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryCreateAPIView(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


# API FOR COMMENT

class StoryCommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=pk)


class PostCommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(story_id=pk)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = CommentSerializer
