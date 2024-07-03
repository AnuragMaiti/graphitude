from django.shortcuts import render
from .models import Graph

def graph_list(request):
    graphs = Graph.objects.all()
    return render(request, 'graph_list.html', {'graphs': graphs})

