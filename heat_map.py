import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from io_utils import read_counts
from smape import symmetric_mean_absolute_percentage_error
import matplotlib.pyplot as plt

hours = [
  "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h",
  "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h", 
  "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"
]
stations = [
  "0000239",
  "0000322",
  "0000174",
  "0000430",
  "0000403",
  "0000369",
  "0000254",
  "0000490",
  "0000468",
  "0000300",
  "0000482",
  "0000463",
  "0000285",
  "0000499",
  "0000410",
  "0000504",
  "0000307",
  "0000262",
  "0000441",
  "0000351",
  "0000483",
  "0000423",
  "0000435",
  "0000495",
  "0000239",
  "0000322",
  "0000174",
  "0000430",
  "0000403",
  "0000369",
  "0000254",
  "0000490",
  "0000468",
  "0000300",
  "0000482",
  "0000463",
  "0000285",
  "0000499",
  "0000410",
  "0000504",
  "0000307",
  "0000262",
  "0000441",
  "0000351",
  "0000483",
  "0000423",
  "0000435",
  "0000495"
]

values = [
  np.random.rand(48) * 2, 
  np.random.rand(48) * 3, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 5, 
  np.random.rand(48) * 6, 
  np.random.rand(48) * 12, 
  np.random.rand(48) * 30, 
  np.random.rand(48) * 29,
  np.random.rand(48) * 25, 
  np.random.rand(48) * 19, 
  np.random.rand(48) * 25, 
  np.random.rand(48) * 15, 
  np.random.rand(48) * 6, 
  np.random.rand(48) * 8, 
  np.random.rand(48) * 9, 
  np.random.rand(48) * 10, 
  np.random.rand(48) * 5, 
  np.random.rand(48) * 3, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 1, 
  np.random.rand(48) * 1,
  np.random.rand(48) * 1,
]

private_values = [
  np.random.rand(48) * 2, 
  np.random.rand(48) * 3, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 5, 
  np.random.rand(48) * 6, 
  np.random.rand(48) * 12, 
  np.random.rand(48) * 30, 
  np.random.rand(48) * 29,
  np.random.rand(48) * 25, 
  np.random.rand(48) * 19, 
  np.random.rand(48) * 25, 
  np.random.rand(48) * 15, 
  np.random.rand(48) * 6, 
  np.random.rand(48) * 8, 
  np.random.rand(48) * 9, 
  np.random.rand(48) * 10, 
  np.random.rand(48) * 5, 
  np.random.rand(48) * 3, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 2, 
  np.random.rand(48) * 1, 
  np.random.rand(48) * 1,
  np.random.rand(48) * 1,
]

fig, ax = plt.subplots()
im = ax.imshow(values )

ax.set_xticks(np.arange(len(stations)), labels=stations)
ax.set_yticks(np.arange(len(hours)), labels=hours)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(hours)):
    for j in range(len(stations)):
        text = ax.text(j, i, "",
                       ha="center", va="center", color="w")

ax.set_title("Relative error of the counting of people on each station per hour (percentage)")
fig.tight_layout()
plt.show()