from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('feed/', views.feed, name='feed'),
    path('filter/<image_id>', views.PictureFilter.as_view(), name='filter')
]