import csv

import numpy as np
fieldnames = ['identifier', 'count']

def read_rides(format_key):
  file = open('../spreadsheets/formated-data-41k.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  rides = []
  for row in csvreader:
    if(row[2] == 'FEMALE'):
      rides.append(
        format_key(row)
      )

  print(rides.__len__())

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

def read_counts_with_identifier(fileName):
  file = open(f'../spreadsheets/{fileName}.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  identifiers = ['0000518', '0000127', '0000168', '0000465', '0000284', '0000462', '0000499', '0000537', '0000402', '0000417', '0000151', '0000444', '0000521', '0000477', '0000426', '0000492', '0000435', '0000318', '0000382', '0000497', '0000285', '0000293', '0000459', '0000519']

  values = np.zeros(24)
  counts = np.zeros((24, 24))

  for row in csvreader:
    identifier = (row[0])[:-4]
    hour = int((row[0])[-3:-1])

    if(identifier in identifiers):
      counts[hour][identifiers.index(identifier)] = float(row[1])
      values[identifiers.index(identifier)] += float(row[1])

  file.close()

  return identifiers, counts, values