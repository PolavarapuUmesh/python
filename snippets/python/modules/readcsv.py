import csv
csv_file_path='/home/umesh/Desktop/python-programs/snippets/python/modules/agri.csv'
with open(csv_file_path,mode='r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        print(row)