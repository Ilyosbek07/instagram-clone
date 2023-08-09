from django.contrib.auth.models import User
from django.db import models
from apps.common.models import BaseModel
from .managers import StoryManager, ProfileManager, PostManager


# User Models
class Gender(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    )


# Profile model yoki User model qaysi bir yaxshi
class Profile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=222)
    image = models.ImageField(
        upload_to="profile/images",
        default="profile/images/default_profile_picture.jpeg",
    )
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=Gender.GENDER_CHOICES)
    email = models.EmailField(max_length=222)
    is_suggestion = models.BooleanField(default=False)
    objects = ProfileManager()

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    profile = models.ForeignKey(
        Profile, related_name="following", on_delete=models.CASCADE
    )
    follower_id = models.ForeignKey(
        Profile, related_name="follower", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.profile.user.username


class Highlight(BaseModel):
    name = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Story(BaseModel):
    profile_id = models.ForeignKey(
        Profile, related_name="story", on_delete=models.CASCADE
    )
    video = models.FileField(upload_to="profile/stories", null=True, blank=True)
    image = models.ImageField(upload_to="profile/story/images")
    highlight = models.ForeignKey(
        Highlight, on_delete=models.CASCADE, null=True, blank=True
    )
    objects = StoryManager()

    def __str__(self):
        return self.profile_id.user.username


# Post Models
class Image(models.Model):
    image_path = models.ImageField(upload_to="post/images")


class Video(models.Model):
    video_path = models.FileField(upload_to="post/videos")


class Post(BaseModel):
    profile = models.ForeignKey(Profile, related_name="post", on_delete=models.CASCADE)
    title = models.CharField(max_length=222)
    images = models.ManyToManyField(Image, blank=True)
    video = models.ManyToManyField(Video, blank=True)
    objects = PostManager()

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()


class Comment(BaseModel):
    profile_id = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL
    )
    post_id = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Saved(models.Model):
    post_id = models.ForeignKey(
        Post, related_name="saved_post", on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        Profile, related_name="saved_profile", on_delete=models.CASCADE
    )
