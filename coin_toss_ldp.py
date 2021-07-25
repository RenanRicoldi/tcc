import torch

def get_private_mean(real_answers):
  first_coin_flip = (torch.rand(len(real_answers)) > 0.5).float()
  second_coin_flip = (torch.rand(len(real_answers)) > 0.5).float()
  private_answers = real_answers.float() * first_coin_flip + (1 - first_coin_flip) * second_coin_flip
  return private_answers.mean() * 2 - 0.5


def get_private_mean_with_noise(real_answers, noise):
  first_coin_flip = (torch.rand(len(real_answers)) > noise).float()
  second_coin_flip = (torch.rand(len(real_answers)) > 0.5).float()
  private_answers = real_answers.float() * first_coin_flip + (1 - first_coin_flip) * second_coin_flip
  return (private_answers.mean()/noise - 0.5) * noise/(1 - noise)

answers = torch.randint(0, 2, (100000, ))
noise = 0.01
print("mean without noise: {}".format(str(answers.float().mean())))
print("mean with 50% noise: {}".format(str(get_private_mean(answers))))
print("mean with {:.0f}% noise: {}".format(noise*100, str(get_private_mean_with_noise(answers, noise))))