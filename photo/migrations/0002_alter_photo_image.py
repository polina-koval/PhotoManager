# Generated by Django 4.1.4 on 2022-12-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(upload_to="photos/"),
        ),
    ]
