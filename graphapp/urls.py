from django.urls import path, include
from graphapp.views import demo_charts
from graphapp.views import csv_form
from graphapp.views import csv_uploader
from graphapp.views import home_page
from graphapp.views import csv_analysis
from graphapp.views import predictive_model


urlpatterns = [
    path("", home_page.index, name="index"),
    path('csvuploader/', csv_uploader.CsvUploader.as_view(), name='csvuploader'),
    # path('csvtableview/', views.CsvTableView, name='csvtableview'),
    # Add more URLs as needed
    path('csvform/', csv_form.dynamic_form_view, name='csvform'),
    path('csvanalysis/', csv_analysis.csv_analysis, name='csvanalysis'),

    path("democharts/", demo_charts.charts_view, name="democharts"),
    path("democharts/filter-options/", demo_charts.get_filter_options, name="demo-chart-filter-options"),
    path("democharts/barchart/<int:year>/", demo_charts.get_bar_chart, name="demo-barchart"),
    path("democharts/linechart/<int:year>/", demo_charts.get_line_chart, name="demo-linechart"),
    path("democharts/piechart/<int:year>/", demo_charts.get_pie_chart, name="demo-piechart"),
    path("democharts/scatterplot/<int:year>/<str:column2>", demo_charts.get_scatter_chart, name="demo-scatterplot"),

    path("csvanalysis/csvfilenames/", csv_analysis.get_csv_file_names, name="csvfilenames"),
    path("csvanalysis/csvcolumnnames/<str:csvfilename>", csv_analysis.get_csv_column_names, name="csvcolumnnames"),
    path("csvanalysis/barchart/<str:csvfilename>/<str:csvcolumnname>/", csv_analysis.get_bar_chart, name="csvbarchart"),
    path("csvanalysis/linechart/<str:csvfilename>/<str:csvcolumnname>/", csv_analysis.get_line_chart, name="csvlinechart"),
    path("csvanalysis/piechart/<str:csvfilename>/<str:csvcolumnname>/", csv_analysis.get_pie_chart, name="csvpiechart"),
    path("csvanalysis/scatterplot/<str:csvfilename>/<str:csvcolumnname>/<str:csvcolumnname2>/", csv_analysis.get_scatter_chart, name="csvscatterplot"),

    path("predictivemodel/buildpredictivemodel/", predictive_model.build_predictive_model, name="buildpredictivemodel"),
    path("predictivemodel/testpredictivemodel/", predictive_model.test_predictive_model, name="testpredictivemodel"),
    path("predictivemodel/testpredictivemodel/models/<str:modelname>/", predictive_model.get_model, name="testpredictivemodelinfo"),
    path("predictivemodel/testpredictivemodel/modelnames/", predictive_model.get_model_names, name="testpredictivemodelnames"),
    
]
