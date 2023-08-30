from django.urls import path
from .views import hello, upload_file

urlpatterns = [
    path('', hello),
    path('upload', upload_file),
]

