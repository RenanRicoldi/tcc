from cProfile import label
from unicodedata import decimal
import numpy as np
from sklearn.metrics import mean_absolute_error
from io_utils import read_counts
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}%".format(x)})

folder = 'woman-by-station-per-hour'
epsilons = ['0.008', '2.251', '13.814']

sorted_counts = np.array(read_counts('{}/sorted-non-private-counts'.format(folder)))
counts = np.array(read_counts('{}/non-private-counts'.format(folder)))

for epsilon in epsilons:
  private_counts = np.array(read_counts('{}/central-private-counts-epsilon-{}'.format(folder, epsilon)))
  local_private_counts = np.array(read_counts('{}/local-private-counts-epsilon-{}'.format(folder, epsilon)))

  print(
    f'central - {epsilon} - {mean_absolute_error(private_counts, sorted_counts)}'
  )

  print(
    f'local - {epsilon} - {mean_absolute_error(local_private_counts, counts)}'
  )

