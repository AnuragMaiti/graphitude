from django.urls import path, include
from graphapp.views import charts
from graphapp.views import csv_form
from graphapp.views import csv_upload
from graphapp.views import home_page


urlpatterns = [
    path("", home_page.index, name="index"),
    path('csvuploader/', csv_upload.CsvUploader.as_view(), name='csvuploader'),
    # path('csvtableview/', views.CsvTableView, name='csvtableview'),
    # Add more URLs as needed
    path('csvform/', csv_form.dynamic_form_view, name='csvform'),

    path("charts/", charts.charts_view, name="graphapp-charts"),
    path("charts/filter-options/", charts.get_filter_options, name="chart-filter-options"),
    path("charts/barchart/<int:year>/", charts.get_bar_chart, name="barchart"),
    path("charts/linechart/<int:year>/", charts.get_line_chart, name="linechart"),
    path("charts/piechart/<int:year>/", charts.get_pie_chart, name="piechart"),
    path("charts/piechart2/<int:year>/", charts.get_pie_chart2, name="piechart2"),
]
