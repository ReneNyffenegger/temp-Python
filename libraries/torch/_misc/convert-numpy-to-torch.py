import numpy
import torch


data_np         = np.array([
                     [1, 2, 3],
                     [4, 5, 6]
                  ])

data_torch = map(torch.tensor, data_np)

print(data_torch)
