# tables.py
import django_tables2 as tables
import csv
from django.db import models

model_datatype_dict = {'bool': models.BooleanField(), 
                    'int':  models.IntegerField(), 
                    'float': models.FloatField(), 
                    'str': models.CharField(max_length=250, null=True, blank=True)}

def load_csv_file(file_path, headers):
    data = []
    with open(file_path, 'r',  encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values = dict(zip(list(headers.values()), list(row.values())))
            if (len(data) > 10):
                break
            data.append(values)
    return data

def add_class_method(cls):
    def mymethod(self):
        super(cls, self).mymethod()
    cls.mymethod = mymethod
    return cls

def define_csv_table_class(headers, data_types):
    attrs = dict((headers[key], tables.Column()) for key in data_types)
    model_class = define_csv_model_class(headers, data_types)
    Meta = type('Meta', (object, ), {'model': model_class})
    attrs['Meta'] = Meta
    table_class = type('CsvFileTable', (tables.Table,), attrs)
    return table_class

def define_csv_model_class(headers,data_types):
    attrs = dict((headers[key], model_datatype_dict[data_types[key]]) for key in data_types)
    attrs['__module__']='graphapp.models'
    # print(attrs)
    model_class = type('CsvFileModel', (models.Model,), attrs)
    return model_class

def load_csv_table(file_path):
    headers, data_types = extract_columns(file_path)
    csv_table_class = define_csv_table_class(headers, data_types)
    csv_data = load_csv_file(file_path, headers)
    csv_table = csv_table_class(data=csv_data)
    return csv_table

def extract_columns(file_path):
    # Initialize a dictionary to store data types inferred from the first few rows
    headers = {}
    data_types = {}
    with open(file_path, 'r',  encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row_num, row in enumerate(reader, start=0):
            for col_num, value in enumerate(row):
                headers[col_num] = str(value)
            break

    with open(file_path, 'r',  encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Read a few rows to infer data types
        num_rows_to_read = 10
        
        for row_num, row in enumerate(reader, start=1):
            if row_num > num_rows_to_read:
                break
            for col_num, value in enumerate(row):
                current_type = type(value).__name__
                if col_num not in data_types:
                    data_types[col_num] = current_type
                else:
                    # If the type inferred from a previous row is different, assume it's a string
                    if data_types[col_num] != current_type:
                        data_types[col_num] = 'str'
    return headers, data_types



# class CsvTable(tables.Table):
#     class Meta:
#         csvModel = 
#         model = CsvModel
#         template_name = "django_tables2/bootstrap4.html"  # Optional: Use Bootstrap 4 styling
#         fields = tuple(columns)  # Specify which fields to include in the table

