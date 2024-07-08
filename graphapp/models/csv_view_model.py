# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class CsvModel(models.Model):
    table_name = models.CharField(max_length=250, null=False, blank=False)
    csv_name = models.CharField(max_length=250, null=False, blank=False)
    data_type = models.TextField(max_length=50,null=False, blank=False)
    sequence_no = models.IntegerField(default=0)
    class Meta:
        ordering = ('-sequence_no',)

    def __str__(self):
        return f"Sequence No: {self.sequence_no} Column: {self.name}, Data Type: {self.data_type}"
