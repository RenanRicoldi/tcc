import numpy as np
from io_utils import read_rides, write_rides
import gc
# from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

def format_key(row):
  return row[0]

rides = read_rides(format_key)

print('rides read')

domain = list(dict.fromkeys(rides))

print('domain defined', len(domain))

levels_of_privacy = [0.501, 0.755, 0.999]

def encode(response):
  return [1 if d == response else 0 for d in domain]

def perturb(encoded_response):
  return [perturb_bit(b) for b in encoded_response]

def perturb_bit(bit):
  sample = np.random.random()
  if bit == 1:
    if sample <= p:
      return 1
    else:
      return 0
  elif bit == 0:
    if sample <= q:
      return 1
    else: 
      return 0

def unary_epsilon(p, q):
  return np.log((p*(1-q)) / ((1-p)*q))

# non private count
non_private_counts = np.sum([encode(ride) for ride in rides], axis=0)

count = list(zip(domain, non_private_counts))

write_rides(count, 'general/non-private-counts')

for p in levels_of_privacy:
  print(f'p = {p}')
  q = 1 - p

  # More RAM

  def aggregate(responses):
    sums = np.sum(responses, axis=0)
    n = len(responses)
    
    return [max(round((v - n*q) / (p-q)), 0) for v in sums]

  responses = [perturb(encode(ride)) for ride in rides]

  gc.collect()
  private_counts = aggregate(responses)

  # Less RAM

  # def aggregate_sums(sums, number_of_responses):
  #   return [round((v - number_of_responses*q) / (p-q)) for v in sums]

  # number_of_responses = 0

  # sums = encode('')
  # for ride in rides:
  #   if(number_of_responses % 1000 == 0):
  #     print(f'{(number_of_responses * 100)/len(rides)}%')
  #   number_of_responses += 1
  #   gc.collect()

  #   # perturb and send to server
  #   response = perturb(encode(ride))

  #   # server receive
  #   sums = np.sum([sums, response], axis=0)

  # private_counts = aggregate_sums(sums, number_of_responses)

  gc.collect()
  private_count = list(zip(domain, private_counts))

  # print('mean absolute percentage error: ', mean_absolute_percentage_error(non_private_counts, private_counts))
  # print('mean absolute error: ', mean_absolute_error(non_private_counts, private_counts))

  write_rides(private_count, 'general/local-private-counts-epsilon-{:.3f}'.format(unary_epsilon(p, q)))