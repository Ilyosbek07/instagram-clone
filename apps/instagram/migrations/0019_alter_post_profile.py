# Generated by Django 4.2.1 on 2023-08-09 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0018_alter_post_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post",
                to="instagram.profile",
            ),
        ),
    ]
