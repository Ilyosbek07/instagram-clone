from django.db import models


class StoryManager(models.Manager):
    def for_active_profiles(self, active_profiles_queryset):
        profile_ids = active_profiles_queryset.values_list("id", flat=True)
        return self.filter(profile_id__in=profile_ids)


class ProfileManager(models.Manager):
    def is_suggested(self):
        return self.order_by("-id").filter(is_suggestion=1).all()


class PostManager(models.Manager):
    def followed_profiles_posts(self, profiles_queryset):
        profile_ids = profiles_queryset.values_list("id", flat=True)
        return self.filter(profile__in=profile_ids)
