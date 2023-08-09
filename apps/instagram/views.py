from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.instagram.models import Profile, Post, Story, Comment, Follow, Like, Saved
from apps.instagram.serializers import (
    ProfileSerializer,
    PostSerializer,
    StorySerializer,
    CommentSerializer,
    RegistrationSerializer,
    LikeSerializer, SavedSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]

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
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]


class ProfileListAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)
        serializer_profile = ProfileSerializer(profile)
        following = Follow.objects.filter(follower_id=profile.id).all()
        following_stories = Story.objects.for_active_profiles(following)
        serializer_story = StorySerializer(instance=following_stories, many=True)
        suggested = Profile.objects.is_suggested()
        serializer_suggested_profiles = ProfileSerializer(suggested, many=True)
        posts = Post.objects.followed_profiles_posts(following)
        serializer_posts = PostSerializer(posts, many=True)
        return Response(
            {
                "story": serializer_story.data,
                "user_profile": serializer_profile.data,
                "suggested_profiles": serializer_suggested_profiles.data,
                "posts": serializer_posts.data,
            },
            template_name="home.html",
        )


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        post_id = request.data.get("post_id")
        user_id = request.data.get("user_id")

        if not post_id or not user_id:
            return Response(
                {"error": "Both post_id and user_id are required."}, status=400
            )
        post = Post.objects.get(id=post_id)
        user = Profile.objects.get(id=user_id)
        like, created = Like.objects.get_or_create(post_id=post, user_id=user)
        if created:
            return redirect("/instagram/v1/post/")
        else:
            like.delete()
            return redirect("/instagram/v1/post/")


class SavedViewSet(ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer

    def post(self, request, *args, **kwargs):
        post_id = request.data.get("post_id")
        user_id = request.data.get("user_id")

        if not post_id or not user_id:
            return Response(
                {"error": "Both post_id and user_id are required."}, status=400
            )
        post = Post.objects.get(id=post_id)
        user = Profile.objects.get(id=user_id)
        saved, created = Saved.objects.get_or_create(post_id=post, user_id=user)
        if created:
            return redirect("/instagram/v1/post/")
        else:
            saved.delete()
            return redirect("/instagram/v1/post/")


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
