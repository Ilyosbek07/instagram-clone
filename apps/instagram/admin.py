from django.contrib import admin
from apps.instagram.models import Post, Profile, Story, Saved, Image, Video, Comment

admin.site.register(Post)
admin.site.register(Story)
admin.site.register(Saved)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Image)
