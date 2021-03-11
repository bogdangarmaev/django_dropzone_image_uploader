from rest_framework import serializers

from apps.image.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Image
