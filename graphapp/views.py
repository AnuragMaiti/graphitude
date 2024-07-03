from django.shortcuts import render
from .models import Graph
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "index.html", context)


