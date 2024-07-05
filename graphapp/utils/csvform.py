import csv

def parse_csv(file_path):
    print(file_path)
    with open(file_path, 'r',  encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames
        data = [row for row in reader]
    return headers, data