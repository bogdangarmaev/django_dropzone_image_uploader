from django.db import models

from PIL import Image as img


class Image(models.Model):
    file = models.ImageField(upload_to='pictures/')

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        image = img.open(self.file.path)
        image.save(self.file.path, quality=20, optimize=True)

