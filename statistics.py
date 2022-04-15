import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from io_utils import read_counts
from smape import symmetric_mean_absolute_percentage_error
import matplotlib.pyplot as plt

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}%".format(x*100)})

counts = np.array([read_counts('count_hour')])
private_counts = np.array([read_counts('private_count_hour-3')])

mae = mean_absolute_error(private_counts, counts, multioutput='raw_values')

mape = mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')

smape = symmetric_mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')

print(
  mean_absolute_error(private_counts, counts, multioutput='raw_values')
)

print(
  mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')
)

print(
  symmetric_mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')
)
fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
ax.set(xlim=(0, 8), xticks=np.arange(1, 8))

# ax.plot(mae, linestyle = 'dotted')
ax.plot(mape, linestyle = 'solid')
ax.plot(smape, linestyle = 'dashed')
plt.show()

# print(
#   alt_mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')
# )

