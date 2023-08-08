from rest_framework import serializers

from apps.instagram.models import Post, Story, Profile, Comment, Image, Video


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'profile_id',
            'post_id',
            'story_id',
            'text'
        )


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    video = VideoSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'user',
            'title',
            'images',
            'video'
        )


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            'image',
            'video'
        )


class ProfileSerializer(serializers.ModelSerializer):
    story = StorySerializer(many=True)
    post = PostSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            'fullname',
            'username',
            'image',
            'bio',
            'gender',
            'email',
            'is_suggestion',
            'story',
            'post'
        )

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
