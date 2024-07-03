from django.shortcuts import render
from .models import Graph
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render
import csv

def index(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "index.html", context)


class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'


    def decode_utf8(self, input_iterator):
        for l in input_iterator:
            yield l.decode('utf-8')

    def post(self, request):
        context = {}
        reader=csv.DictReader(self.decode_utf8(request.FILES['csv']))
        for row in reader:
            header = list(row.keys())
            print(header)
            break
        data = []
        for row in reader:
            values = list(row.values())
            data.append(values)
        context['header'] = header
        context['data'] = data
        return render(request, self.template_name, context)

