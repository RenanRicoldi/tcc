import csv

import numpy as np
fieldnames = ['identifier', 'count']

def read_rides(format_key):
  file = open('../spreadsheets/formated-data-100k.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  rides = []
  for row in csvreader:
    rides.append(
      format_key(row)
    )

  file.close()

  return rides

def write_rides(rows, filename):
  with open(f'../spreadsheets/{filename}.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(rows)

def read_counts(fileName):
  file = open(f'../spreadsheets/{fileName}.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  counts = []
  for row in csvreader:
    counts.append(float(row[1]))

  file.close()

  return counts