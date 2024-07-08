from django.urls import path
from . import views

urlpatterns = [
    path('graphs/', views.graph_list, name='graph_list'),
    # Add more URLs as needed
]
