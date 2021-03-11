from django.views.generic import TemplateView
from rest_framework.generics import CreateAPIView

from apps.image.models import Image
from apps.image.serializers import ImageSerializer


class ImageCreateView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageView(TemplateView):
    template_name = 'upload_form.html'
