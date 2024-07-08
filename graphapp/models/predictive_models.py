from django.db import models

class PredictiveModel(models.Model):
    name = models.CharField(max_length=250)
    csv_file_name = models.CharField(max_length=250)
    properties_json = models.TextField()
