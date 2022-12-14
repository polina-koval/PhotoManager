from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Photo(models.Model):
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    people = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to="photos/")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return self.user.username
