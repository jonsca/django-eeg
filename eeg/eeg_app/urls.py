from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('upload', views.upload_file, name='upload'),
    path('post_upload', views.post_upload, name='post.upload'),
    path('download_file', views.download_file, name='download.file'),
    path('register', views.SignupView.as_view(), name='register')
]