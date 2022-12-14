from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Photo(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    people = models.CharField(max_length=255)
    image = models.FileField(upload_to="photos/")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return self.description
