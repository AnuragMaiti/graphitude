from django.apps import AppConfig
from django.contrib import admin


class GraphappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'graphapp'
    verbose_name = 'Graphitude Administration'

    # Customize admin site title and header
    def ready(self):
        admin.site.site_title = 'Graphitude'
        admin.site.site_header = 'Graphitude Administration'
        admin.site.index_title = 'Graphitude Security'
        admin.site.site_url = '/graphapp/charts'
