import numpy
import torch


data_np    = numpy.array([
                     [1, 2, 3],
                     [4, 5, 6]
                  ])

data_torch = list(map(torch.tensor, [ data_np ] ))

print(data_torch)
