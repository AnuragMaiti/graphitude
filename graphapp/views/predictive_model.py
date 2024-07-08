# views.py

from django import forms
from graphapp.models import PredictiveModel
from django.shortcuts import render
from django.shortcuts import render

class PredictiveModelForm(forms.Form):
    selected_columns = forms.ModelMultipleChoiceField(queryset=PredictiveModel.objects.all(), widget=forms.CheckboxSelectMultiple)

def build_predictive_model(request):
    if request.method == 'POST':
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

