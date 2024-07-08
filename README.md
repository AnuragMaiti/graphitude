# graphitude
A website which helps you to visualise data.

# Create a virtual environment (optional but recommended)
python -m venv venv_graphitude
# On Windows: python -m venv venv_graphitude

# Activate the virtual environment
# On macOS/Linux:
source ./venv_graphitude/bin/activate
# On Windows (cmd.exe):
venv_graphitude\Scripts\activate.bat
# On Windows (PowerShell):
venv_graphitude\Scripts\Activate.ps1


# Create a new directory for your project. If you have git repository then may avoid creating directory
mkdir graphitude
cd graphitude


# Install Django
pip install django

# Create a new Django project named 'graphitude'
django-admin startproject graphitude .
# Note the dot (.) at the end, which ensures Django creates files in the current directory


