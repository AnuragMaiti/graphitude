from django.shortcuts import render
from graphapp.utils import dynamic_form_class
from graphapp.utils import parse_csv
from django.core.files.storage import FileSystemStorage

def dynamic_form_view(request):
    if request.method == 'POST':
        form = dynamic_form_class(request.POST)
        # if form.is_valid():
            # Process the form data
            # Example: Save to database
            # form.cleaned_data contains the validated data
        return render(request, 'result.html', {'data': form})
    else:
        file_name = 'CarPrice.csv'
        fs = FileSystemStorage()
        file_path = fs.path(file_name)
        headers, _ = parse_csv(file_path)
        form_class = dynamic_form_class(headers)
        form = form_class()
    return render(request, 'dynamic_form.html', {'form': form})

