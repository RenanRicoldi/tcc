from cProfile import label
from unicodedata import decimal
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from io_utils import read_counts
from smape import symmetric_mean_absolute_percentage_error
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}%".format(x)})

epsilon = '2.251'

counts = np.array([read_counts('by-hour/non-private-counts')])
private_counts = np.array([read_counts('by-hour/central-private-counts-epsilon-{}'.format(epsilon))])
local_private_counts = np.array([read_counts('by-hour/local-private-counts-epsilon-{}'.format(epsilon))])

# mae = mean_absolute_error(private_counts, counts, multioutput='raw_values')

# mape = mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')

print(private_counts, counts)
smape = symmetric_mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')
local_smape = symmetric_mean_absolute_percentage_error(local_private_counts, counts, multioutput='raw_values')

# print(
#   mean_absolute_error(private_counts, counts, multioutput='raw_values')
# )

# print(
#   mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')
# )

# print(
#   symmetric_mean_absolute_percentage_error(private_counts, counts, multioutput='raw_values')*100
# )

fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
ax.set(xlim=(0, 23), xticks=np.arange(0, 23))


# sMAPE
# ax.set_ylabel('sMAPE (%)')
# ax.set_xlabel('Horas do dia')
# ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

# ax.plot(smape*100, linestyle = 'solid', label='Central')
# ax.plot(local_smape*100, linestyle = 'dashed', label='Local')

# ax.grid(True)
# ax.legend()

# plt.title('ε = {}'.format(epsilon))
# plt.show()