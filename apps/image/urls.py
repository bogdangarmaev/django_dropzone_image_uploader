from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageView.as_view()),
    path('upload/', views.ImageCreateView.as_view(), name='upload_image'),
]
