import csv
fieldnames = ['identifier', 'count']

def format_key(station_id, hour, gender):
  return f'{station_id:07d}-{hour:02d}-{gender}'


def read_rides():
  file = open('../spreadsheets/formated_rides.csv')
  csvreader = csv.reader(file)

  next(csvreader)

  rides = []
  for row in csvreader:
    rides.append(
      f'{row[0]}-{row[1]}-{row[2]}'
    )

  file.close()

  return rides

def write_rides(rows, filename):
  with open(f'../spreadsheets/{filename}.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(rows)

