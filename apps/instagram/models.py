from django.db import models
from apps.common.models import BaseModel


# User Models
class Gender(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )


class Profile(BaseModel):
    fullname = models.CharField(max_length=222)
    username = models.CharField(max_length=222)
    image = models.ImageField(upload_to="profile/images", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=Gender.GENDER_CHOICES)
    email = models.EmailField(max_length=222)
    is_suggestion = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Follow(models.Model):
    profile = models.ForeignKey(Profile,related_name='following', on_delete=models.CASCADE)
    follower_id = models.ForeignKey(Profile,related_name='follower', on_delete=models.CASCADE)


# class Highlight(BaseModel):
#     name = models.CharField(max_length=222)
#     profile_id = models.ForeignKey(Profile, related_name='post', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


class Story(BaseModel):
    profile_id = models.ForeignKey(Profile, related_name='story', on_delete=models.CASCADE)
    video = models.FileField(upload_to="profile/stories", null=True, blank=True)
    image = models.ImageField(upload_to="profile/story/images")
    # highlight = models.ForeignKey(Highlight, on_delete=models.SET_NULL)


# Post Models
class Image(models.Model):
    image_path = models.ImageField(upload_to="post/images")


class Video(models.Model):
    video_path = models.FileField(upload_to="post/videos")


class Post(BaseModel):
    user = models.ForeignKey(Profile, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=222)
    images = models.ManyToManyField(Image, null=True, blank=True)
    video = models.ManyToManyField(Video, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    profile_id = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    post_id = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    story_id = models.ForeignKey(Story, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Saved(models.Model):
    post_id = models.ForeignKey(Post, related_name='saved_post', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, related_name='saved_profile', on_delete=models.CASCADE)
