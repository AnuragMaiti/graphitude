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
from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
from django.core.files.storage import FileSystemStorage
from graphapp.utils.csvform import parse_headers
from graphapp.utils.csvtable import prepare_chart_data

@staff_member_required
def get_csv_file_names(request):
    fs = FileSystemStorage()
    file_path = fs.path('.')
    all_dir_files = fs.listdir(file_path)
    options = all_dir_files[1]
    return JsonResponse({
        "options": options,
    })

@staff_member_required
def get_csv_column_names(request, csvfilename):
    fs = FileSystemStorage()
    csv_file = fs.path(csvfilename)
    column_names = parse_headers(csv_file)
    options = column_names
    return JsonResponse({
        "options": options,
    })

@staff_member_required
def get_bar_chart(request, csvfilename, csvcolumnname):
    chart_data = prepare_chart_data(csvfilename, csvcolumnname)
    return JsonResponse({
        "title": f"Bar Chart for file: {csvfilename} and column: {csvcolumnname}",
        "data": {
            "labels": list(chart_data.keys()),
            "datasets": [{
                "label": "Bar Chart($)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data.values()),
            }]
        },
    })



@staff_member_required
def get_line_chart(request, csvfilename, csvcolumnname):
    print(csvfilename)
    print(csvcolumnname)
    
    chart_data = prepare_chart_data(csvfilename, csvcolumnname)
    return JsonResponse({
        "title": f"Line Chart for {csvfilename} - {csvcolumnname}",
        "data": {
            "labels": list(chart_data.keys()),
            "datasets": [{
                "label": "-",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data.values()),
            }]
        },
    })


@staff_member_required
def get_pie_chart(request, csvfilename, csvcolumnname):
    chart_data = prepare_chart_data(csvfilename, csvcolumnname)
    return JsonResponse({
        "title": f"Pie Chart for {csvfilename} - {csvcolumnname}",
        "data": {
            "labels": ["Successful", "Unsuccessful"],
            "datasets": [{
                "label": "-",
                "backgroundColor": [colorSuccess, colorDanger],
                "borderColor": [colorSuccess, colorDanger],
                "data": chart_data,
            }]
        },
    })


@staff_member_required
def get_pie_chart2(request, csvfilename, csvcolumnname):
    chart_data = prepare_chart_data(csvfilename, csvcolumnname)
    return JsonResponse({
        "title": f"Pie Chart for {csvfilename} - {csvcolumnname}",
        "data": {
            "labels": list(chart_data.keys()),
            "datasets": [{
                "label": "-",
                "backgroundColor": generate_color_palette(len(chart_data)),
                "borderColor": generate_color_palette(len(chart_data)),
                "data": list(chart_data.values()),
            }]
        },
    })


@staff_member_required
def csv_analysis(request):
    return render(request, "csv_analysis.html", {})
