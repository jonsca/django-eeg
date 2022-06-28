from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('post_upload', views.post_upload, name='post_upload')
]