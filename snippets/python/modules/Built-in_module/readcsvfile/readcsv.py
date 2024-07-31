import csv
csv_file_path='/home/umesh/Desktop/python-programs/snippets/python/modules/Built-in_module/readcsvfile/agri.csv'
with open(csv_file_path,mode='r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for read in csv_reader:
        print(read)