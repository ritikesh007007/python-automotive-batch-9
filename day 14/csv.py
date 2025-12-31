import csv

filename="test.csv"
fields=[]
row=[]
with open(filename, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    
    for row in csvreader:
        rows.append(row)
         

