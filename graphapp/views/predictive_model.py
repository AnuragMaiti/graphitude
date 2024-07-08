# views.py

from django import forms
from graphapp.models import PredictiveModel
from django.shortcuts import render
from django.shortcuts import render
import json
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


class PredictiveModelForm(forms.Form):
    selected_columns = forms.ModelMultipleChoiceField(queryset=PredictiveModel.objects.all(), widget=forms.CheckboxSelectMultiple)

def build_predictive_model(request):
    if request.method == 'POST':
        selected_columns=[]
        for key in request.POST:
            # Example: All dynamically generated column fields start with 'graphapp_column_'
            if key.startswith('graphapp_form_model_column_'):
                column_name = request.POST[key]
                selected_columns.append(column_name)

        graphapp_form_file_name = request.POST['graphapp_form_file_name']
        graphapp_form_model_name = request.POST['graphapp_form_model_name']
        graphapp_form_target_column_name = request.POST['graphapp_form_target_column_name']
        graphapp_form_predictive_model_algorithm = request.POST['graphapp_form_predictive_model_algorithm']
        
        model_json = {}
        model_json['graphapp_form_file_name'] = graphapp_form_file_name
        model_json['graphapp_form_model_name'] = graphapp_form_model_name
        model_json['graphapp_form_target_column_name'] = graphapp_form_target_column_name
        model_json['graphapp_form_predictive_model_algorithm'] = graphapp_form_predictive_model_algorithm
        model_json['selected_columns'] = selected_columns
        json_string = json.dumps(model_json)
        fs = FileSystemStorage()
        with fs.open(f"models/{graphapp_form_model_name}.json", 'w') as file:
              file.write(json_string)

        print(graphapp_form_file_name)
        print(graphapp_form_model_name)
        print(graphapp_form_target_column_name)
        print(graphapp_form_predictive_model_algorithm)
        print(selected_columns)

        form = PredictiveModelForm(request.POST)
        if form.is_valid():
            selected_columns = form.cleaned_data['selected_columns']
            # Process selected rows as needed
            return render(request, 'build_predictive_model.html', {'selected_columns': selected_columns})
    else:
        form = PredictiveModelForm()

    return render(request, 'build_predictive_model.html', {'form': form})


def test_predictive_model(request):
    if request.method == 'POST':
        form = PredictiveModelForm(request.POST)
        if form.is_valid():
            selected_columns = form.cleaned_data['selected_columns']
            # Process selected rows as needed
            return render(request, 'test_predictive_model.html', {'selected_columns': selected_columns})
    else:
        form = PredictiveModelForm()

    return render(request, 'test_predictive_model.html', {'form': form})


def get_model_names(request):
    fs = FileSystemStorage()
    file_path = fs.path('models')
    all_dir_files = fs.listdir(file_path)
    model_names_json = all_dir_files[1]
    model_names = [x[:-5] for x in model_names_json]
    return JsonResponse({
        "options": model_names,
    })