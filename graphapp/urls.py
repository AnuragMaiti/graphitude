from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('csvuploader/', views.CsvUploader.as_view(), name='csvuploader'),
    # path('csvtableview/', views.CsvTableView, name='csvtableview'),
    # Add more URLs as needed
]
