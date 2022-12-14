from django.contrib.auth import get_user_model
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

User = get_user_model()


class Photo(models.Model):
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    people = ArrayField(
        models.CharField(max_length=255), default=list, blank=True, null=True
    )
    image = models.FileField(upload_to="photos/")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return self.user.username
