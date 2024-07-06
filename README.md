# Graphitude
Welcome to Graphitude, a dynamic website that helps you to visualise your data! Simply upload your dataset and choose the column you wish to visualise and the type of visualisation. You can also select custom columns to generate a model and use it to predict values.



# Quick Start
## Create a virtual environment (optional but recommended)
python -m venv venv_graphitude
## On Windows: python -m venv venv_graphitude

## Activate the virtual environment
## On macOS/Linux:
source ./venv_graphitude/bin/activate
## On Windows (cmd.exe):
venv_graphitude\Scripts\activate.bat
## On Windows (PowerShell):
venv_graphitude\Scripts\Activate.ps1


## Create a new directory for your project. If you have git repository then may avoid creating directory
mkdir graphitude
cd graphitude


## Install Django
pip install django

## Git clone
clone from 

## Create a new Django project named 'graphitude'
django-admin startproject graphitude .
## Note the dot (.) at the end, which ensures Django creates files in the current directory


## Run the server
python manage.py runserver



# PART-2

### Step 1: Navigate to your existing Django project

Assuming you already have the `graphitude` project set up, navigate to its directory in your terminal:

bash

Code:

`cd path/to/your/graphitude`

### Step 2: Create the Django app

1.  **Create a Django app named `graphapp`:** Inside your project directory (`graphitude`), run:
bash Code:
    
    `python manage.py startapp graphapp`
    
    This will create a directory named `graphapp`.
    
2.  **Register the app in Django settings:** Open `graphitude/settings.py` and add `'graphapp',` to the `INSTALLED_APPS` list:
    
    python
    Code:
    
    `INSTALLED_APPS = [     ...     'graphapp',     ... ]`
    

### Step 3: Define models (if needed)

If your app `graphapp` needs models, define them in `graphapp/models.py`. For example:

Python Code:

`from django.db import models  class Graph(models.Model):     name = models.CharField(max_length=100)     description = models.TextField()      def __str__(self):         return self.name`

After defining models, you'll need to create and apply migrations:

bash Code:

`python manage.py makemigrations graphapp
 python manage.py migrate`

### Step 4: Create views

Define views in `graphapp/views.py`. Here's an example view:

python

Code:

`from django.shortcuts import render from .models import Graph  def graph_list(request):     graphs = Graph.objects.all()     return render(request, 'graphapp/graph_list.html', {'graphs': graphs})`

### Step 5: Create templates

1.  **Create templates directory:** Inside the `graphapp` directory, create a new directory named `templates`.
    
2.  **Create HTML template:** Inside `graphapp/templates`, create `graph_list.html` (or any other needed templates):
    
    html
    
    Code:
    
    `<!DOCTYPE html> <html> <head>     <title>Graph List</title> </head> <body>     <h1>Graph List</h1>     <ul>         {% for graph in graphs %}             <li>{{ graph.name }}</li>         {% endfor %}     </ul> </body> </html>`
    

### Step 6: Define URLs

1.  **Create `urls.py` in `graphapp`:** Create a new file `urls.py` inside the `graphapp` directory and define your URLs:
    
    python
    
    Code:
    
    `from django.urls import path from . import views  urlpatterns = [     path('graphs/', views.graph_list, name='graph_list'),     # Add more URLs as needed ]`
    
2.  **Include `graphapp` URLs in project URLs:** Open `graphitude/urls.py` and include the `graphapp` URLs:
    
    python
    
    Code:
    
    `from django.contrib import admin from django.urls import path, include  urlpatterns = [     path('admin/', admin.site.urls),     path('graphapp/', include('graphapp.urls')),     # Add other URL patterns as needed ]`
    

### Step 7: Run your Django development server

1.  **Run the server:**
    
    bash
    
    Code:
    
    `python manage.py runserver`
    
2.  **Access your app:** Go to `http://127.0.0.1:8000/graphapp/graphs/` (or the URL defined in your `urls.py`).
    

### Step 8: Further development

Now that your `graphapp` app is integrated into your existing `graphitude` project, you can continue to develop additional features, templates, views, and models as per your project requirements.
