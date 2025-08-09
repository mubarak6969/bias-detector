from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for home page
    path('upload/', views.upload_file, name='upload_file'),
]