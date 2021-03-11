from django.contrib import admin

from apps.image.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Represents UI for `Image`
    """
    pass
