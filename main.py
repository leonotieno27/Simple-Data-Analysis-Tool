import csv
import statistics

file_name = "math.csv"
column_index = 0
values = []

with open (file_name, 'r') as csvfile: #load csv file
    csvreader = csv.reader(csvfile)
    next(csvreader) #skip header
    for row in csvreader:
        values.append(float(row[column_index])) #append values in column 0, first column

mean_value = sum(values) / len(values) #mean total sum divide total length
print(f'Mean: {mean_value}')

median_value = statistics.median(values) #importing median from statistics library
print(f"Median: {median_value}")

