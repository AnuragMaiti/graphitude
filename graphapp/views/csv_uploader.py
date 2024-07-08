from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
import io
from django.shortcuts import render
import csv
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render
from graphapp.utils.csvtable import load_csv_table


from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

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
            context['csv_file_name'] = saved_file
            return render(request, self.template_name, context)
        return render(request, self.template_name,context)
    
    def get(self, request):
        context = {}
        if(request.GET):
            csv_file_name = request.GET['csv_file_name']
            fs = FileSystemStorage()
            file_path = fs.path(csv_file_name)
            csv_table =  load_csv_table(file_path)
            # print(csv_table)
            context['table'] = csv_table
            context['csv_file_name'] = csv_file_name
        return render(request, self.template_name,context)

