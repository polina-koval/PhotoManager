from django.contrib import admin
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ["user", "description", "people", "get_preview_img"]
    list_filter = ["user", "date"]

    def get_preview_img(self, obj: Photo):
        if obj.image:
            return mark_safe(f"<img src = {obj.image.url} width=200>")

    get_preview_img.short_description = "Image"
