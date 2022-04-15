import csv

import numpy as np
fieldnames = ['identifier', 'count']

# def format_key(station_id, hour, gender):
#   return f'{station_id:07d}-{hour:02d}'

def format_key(station_id, hour, gender):
  return f'{hour:02d}'

def read_rides():
  file = open('../spreadsheets/formated_rides.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  rides = []
  for row in csvreader:
    rides.append(
      format_key(row[0],int(row[1]),row[2])
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