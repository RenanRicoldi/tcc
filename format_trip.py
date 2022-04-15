import csv
fieldnames = ['station_id', 'hour', 'gender', 'user_type', 'birth_year']

file = open('../spreadsheets/tripdata.csv')
csvreader = csv.reader(file)

with open(f'../spreadsheets/formated_rides.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(fieldnames)

  next(csvreader)

  counter = 0

  for row in csvreader:
    counter += 1
    if(counter > 10000):
      break

    if(row[3] != 'NULL'):
      station_id = int(row[3])
    else:
      station_id = 0

    if(row[14] == '1'):
      gender = 'MALE'
    else:
      gender = 'FEMALE'

    hour = (row[1].split(' ')[1]).split(':')[0]

    writer.writerow(
      [f'{station_id:07d}', hour, gender, row[12], row[13]]
    )

  file.close()
