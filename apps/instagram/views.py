from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.instagram.models import Profile, Post, Story, Comment
from apps.instagram.serializers import (
    ProfileSerializer,
    PostSerializer,
    StorySerializer,
    CommentSerializer,
    RegistrationSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        context = {"data": serializer}
        return Response(context, template_name="login.html")

    @action(detail=False, methods=["post"], serializer_class=RegistrationSerializer)
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"data": serializer.data}, template_name="login.html")

    @action(detail=False, methods=["post"], serializer_class=RegistrationSerializer)
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/instagram/v1/post/")
        else:
            return Response(
                {"error": "Iltimos parol yoki usernameni qaytadan tekshiring !"},
                template_name="login.html",
            )


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
            "message": "Hello, Django!",
        }
        return render(request, "home.html", context)


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
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(post_id=pk)


class PostCommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(story_id=pk)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = CommentSerializer
