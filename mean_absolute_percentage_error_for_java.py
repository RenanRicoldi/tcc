from csv import reader
from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error
# import matplotlib.pyplot as plt
# import numpy as np
# import hashlib

# plt.style.use('_mpl-gallery')

# x = []
# y = []

def read_rides(filename):
  file = open(f'../spreadsheets/{filename}.csv')
  csvreader = reader(file)

  next(csvreader)

  rides = []
  for row in csvreader:
    rides.append(
     int(row[1])
    )
    # x.append(hashlib.md5(row[0].encode()))
    # y.append(int(row[1]))

  file.close()

  return rides

non_private_counts = read_rides('non_private_counts_per_station')
private_counts = read_rides('private_counts_per_station')

print(non_private_counts[0:10])
print(private_counts[0:10])

print('mean absolute percentage error: ', mean_absolute_percentage_error(non_private_counts, private_counts))
print('mean absolute error: ', mean_absolute_error(non_private_counts, private_counts))

# fig, ax = plt.subplots(figsize=(20, 10), layout='constrained')

# ax.plot(np.arange(0, len(x)), y, linewidth=1.0)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 100),
#        ylim=(0, 8), yticks=np.arange(1, 100))

# plt.show()