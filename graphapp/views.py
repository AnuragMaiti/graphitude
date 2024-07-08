from django.shortcuts import render
from .models import Graph
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
import io
from django.shortcuts import render
import csv
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from .tables import load_csv_table

def index(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "index.html", context)


class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'
    # template_name = 'csv_table_view.html'

    def decode_utf8(self, input_iterator):
        for l in input_iterator:
            yield l.decode('utf-8')

    def post(self, request):
        context={}
        csv_file = request.FILES['csv'] if 'csv' in request.FILES else None
        if csv_file:
            # save attached file
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            saved_file = fs.save(csv_file.name, csv_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            # file_url = fs.url(saved_file)
            file_path = fs.path(saved_file)
            csv_table =  load_csv_table(file_path)
            # print(csv_table)
            context['table'] = csv_table
            return render(request, self.template_name, context)
  
        return render(request, self.template_name,context)


    def post_raw_process(self, request):
        csv_file = request.FILES['csv'] if 'csv' in request.FILES else None
        if csv_file:
            # save attached file
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            saved_file = fs.save(csv_file.name, csv_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            # file_url = fs.url(saved_file)
            file_path = fs.path(saved_file)
            with open(file_path, 'r',  encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    header = list(row.keys())
                    break
                data = []
                for row in reader:
                    values = list(row.values())
                    data.append(values)
        context={}
        context['header'] = header
        context['data'] = data
        return render(request, self.template_name, context)
