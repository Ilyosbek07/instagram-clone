# Generated by Django 4.2.1 on 2023-08-09 10:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0016_alter_profile_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="user",
            new_name="profile",
        ),
    ]