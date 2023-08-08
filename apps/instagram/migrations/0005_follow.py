# Generated by Django 4.2.4 on 2023-08-07 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0004_alter_post_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "follower_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to="instagram.profile",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to="instagram.profile",
                    ),
                ),
            ],
        ),
    ]
