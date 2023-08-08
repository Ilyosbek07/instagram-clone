# Generated by Django 4.2.1 on 2023-08-08 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0005_follow"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="story_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="instagram.story",
            ),
        ),
    ]