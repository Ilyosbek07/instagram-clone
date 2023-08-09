from django.contrib.auth.models import User
from rest_framework import serializers

from apps.instagram.models import Post, Story, Profile, Comment, Image, Video, Like, Saved


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("profile_id", "post_id", "story_id", "text")


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        password = self.validated_data["password"]
        account = User(username=self.validated_data["username"])
        account.set_password(password)
        account.save()
        return account


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    video = VideoSerializer(many=True)
    username = serializers.CharField(source="profile.user.username", read_only=True)
    photo_of_profile = serializers.ImageField(source="profile.image", read_only=True)
    likes_count = serializers.CharField(source="like_count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "profile",
            "title",
            "images",
            "video",
            "username",
            "photo_of_profile",
            "likes_count",
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post_id", "user_id"]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("profile_id", "image", "video", "highlight")

    def to_representation(self, instance):
        data_of_profile = {
            "photo": instance.profile_id.image,
            "username": instance.profile_id.user.username,
        }
        return data_of_profile


class ProfileSerializer(serializers.ModelSerializer):
    story = StorySerializer(many=True)
    post = PostSerializer(many=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "username",
            "fullname",
            "image",
            "bio",
            "gender",
            "email",
            "is_suggestion",
            "story",
            "post",
        )

class SavedSerializer(serializers.ModelSerializer):
    post_id = PostSerializer()
    user_id = ProfileSerializer()

    class Meta:
        model = Saved
        fields = ['post_id', 'user_id']

# class PostReelsSerializer(serializers.ModelSerializer):
# post = serializers.StringRelatedField(many=True)

# class Meta:
#     model = Post
#     fields = (
#         'user',
#         'title',
#         'images',
#         'video'
#     )
