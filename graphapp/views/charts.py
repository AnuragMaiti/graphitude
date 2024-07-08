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
    # grouped_purchases = Purchase.objects.annotate(year=ExtractYear("time")).values("year").order_by("-year").distinct()
    # options = [purchase["year"] for purchase in grouped_purchases]
    options = [2000, 2001, 2002]
    return JsonResponse({
        "options": options,
    })


@staff_member_required
def get_bar_chart(request, year):
    chart_data =  {1:2,3:4,5:6,'successful':True}
    return JsonResponse({
        "title": f"For Bar Chart in {year}",
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
def get_line_chart(request, year):
    chart_data =  {1:2,3:4,5:6,'successful':True}
    return JsonResponse({
        "title": f"For Line Chart in {year}",
        "data": {
            "labels": list(chart_data.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(chart_data.values()),
            }]
        },
    })


@staff_member_required
def get_pie_chart(request, year):
    chart_data = [{1:2,3:4,5:6,'successful':True},{1:2,3:4,5:6,'successful':True},{1:2,3:4,5:6,'successful':True},{1:2,3:4,5:6,'successful':False},]

    return JsonResponse({
        "title": f"For Pie Chart in {year}",
        "data": {
            "labels": ["Successful", "Unsuccessful"],
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": [colorSuccess, colorDanger],
                "borderColor": [colorSuccess, colorDanger],
                "data": [3,4
                    # chart_data.filter(successful=True).count(),
                    # chart_data.filter(successful=False).count(),
                ],
            }]
        },
    })


@staff_member_required
def get_pie_chart2(request, year):
    chart_data = {1:2,3:4,5:6}
    return JsonResponse({
        "title": f"For Pie Chart2  in {year}",
        "data": {
            "labels": list(chart_data.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": generate_color_palette(len(chart_data)),
                "borderColor": generate_color_palette(len(chart_data)),
                "data": list(chart_data.values()),
            }]
        },
    })


@staff_member_required
def charts_view(request):
    return render(request, "charts.html", {})
