from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('csvuploader/', views.CsvUploader.as_view(), name='csvuploader'),
    # Add more URLs as needed
]
