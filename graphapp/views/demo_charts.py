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


@staff_member_required
def get_filter_options(request):
    years = [2000, 2001, 2002]
    return JsonResponse({
        "options": years,
    })


@staff_member_required
def get_bar_chart(request, year):
    chart_data =  {1:2,3:4,5:6,7:9}
    return JsonResponse({
        "title": f"For Bar Chart in {year}",
        "data": {
            "labels": list(chart_data.keys(),),
            "datasets": [{
                "label": "Bar Chart",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data.values(),),
            }]
        },
    })


@staff_member_required
def get_line_chart(request, year):
    chart_data =  {1:2,3:4,5:6,7:8}
    return JsonResponse({
        "title": f"For Line Chart in {year}",
        "data": {
            "labels": list(chart_data.keys(),),
            "datasets": [{
                "label": "Line Chart",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data.values(),),
            }]
        },
    })


@staff_member_required
def get_pie_chart(request, year):
    chart_data =  {1:2,3:4,5:6,7:8}
    return JsonResponse({
        "title": f"For Pie Chart in {year}",
        "data": {
            "labels": list(chart_data.keys(),),
            "datasets": [{
                "label": "Pie Chart",
                "backgroundColor":generate_color_palette(len(chart_data)),
                "borderColor": generate_color_palette(len(chart_data)),
                "data": list(chart_data.values(),),
            }]
        },
    })


@staff_member_required
def get_scatter_chart(request, year, column2):
    chart_data = [{'x':2,'y':5}, {'x':11,'y':15}, {'x':21,'y':52}, {'x':31,'y':54}]
    return JsonResponse({
        "title": f"For Scatter Plot in {year} - {column2}",
        "data": {
            "datasets": [{
                "label": "Scatter Plot",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data,),
            }]
        },
    })


@staff_member_required
def charts_view(request):
    return render(request, "demo_charts.html", {})
