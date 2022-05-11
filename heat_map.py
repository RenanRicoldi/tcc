import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from io_utils import read_counts, read_counts_with_identifier
from smape import symmetric_mean_absolute_percentage_error
import matplotlib.pyplot as plt

hours = [
  "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h",
  "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h", 
  "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"
]

stations, counts, values = read_counts_with_identifier('by-station-per-hour/non-private-counts')
private_stations, private_counts, private_values = read_counts_with_identifier('by-station-per-hour/central-private-counts-epsilon-13.814')

compared_stations = []

for i in range(24):
  compared_stations.append(
    mean_absolute_error(np.array([private_counts[i]]), np.array([counts[i]]), multioutput='raw_values')
  )


fig, ax = plt.subplots()
im = ax.imshow(compared_stations)

ax.set_xticks(np.arange(24), labels=values)
ax.set_yticks(np.arange(24), labels=hours)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(24):
    for j in range(24):
        text = ax.text(j, i, "",
                       ha="center", va="center", color="w")

ax.set_title("Relative error of the counting of people on each station per hour (percentage)")
fig.tight_layout()
plt.show()