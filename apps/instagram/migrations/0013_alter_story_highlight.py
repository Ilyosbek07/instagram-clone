# Generated by Django 4.2.1 on 2023-08-09 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0012_highlight_story_highlight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="highlight",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="instagram.highlight",
            ),
        ),
    ]