from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ["user", "description", "people"]
