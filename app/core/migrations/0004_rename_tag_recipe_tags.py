# Generated by Django 3.2.25 on 2024-03-20 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_auto_20240315_0607"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="tag",
            new_name="tags",
        ),
    ]