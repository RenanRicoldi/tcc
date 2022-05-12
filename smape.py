import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

# def alt_mean_absolute_percentage_error(
#   y_true, y_pred, *, sample_weight=None, multioutput="uniform_average"
# ):
#   epsilon = np.finfo(np.float64).eps
#   mape = np.abs(y_pred - y_true) / np.maximum(np.abs(y_true), epsilon)
#   output_errors = np.average(mape, weights=sample_weight, axis=0)
#   if isinstance(multioutput, str):
#     if multioutput == "raw_values":
#       return np.divide(mape, [len(output_errors)] * len(output_errors))
#     elif multioutput == "uniform_average":
#       # pass None as weights to np.average: uniform mean
#       multioutput = None

#   return np.average(output_errors, weights=multioutput)

def symmetric_mean_absolute_percentage_error(
  y_true, y_pred, *, sample_weight=None, multioutput="uniform_average"
):
  mape = np.abs(y_pred - y_true) / (np.maximum((y_pred + y_true), 1) / 2)
  output_errors = np.average(mape, weights=sample_weight, axis=0)
  if isinstance(multioutput, str):
    if multioutput == "raw_values":
      return output_errors
    elif multioutput == "uniform_average":
      # pass None as weights to np.average: uniform mean
      multioutput = None

  return np.average(output_errors, weights=multioutput)

arr_true = np.array([[3, 1, 5]])
arr_pred = np.array([[3, 6, 1]])

print(
  symmetric_mean_absolute_percentage_error(arr_true, arr_pred, multioutput='raw_values')
)

# print(
#   mean_absolute_percentage_error(arr_true, arr_pred, multioutput='uniform_average')
# )

# (4-3) / 4 = 0.25
# (5-6) / 5 = 0.20
# (6-1) / 6 = 0.83
# 0.25 + 0.2 + 0.83 = 1.28
# 1.28 / 3 = 0.427