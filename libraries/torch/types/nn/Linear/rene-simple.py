import torch

n_input  = 20
n_output = 15

lin = torch.nn.Linear(n_input, n_output)

print(type(lin.bias  ))
print(type(lin.weight))

print('------------------------------')

print(lin.bias  .shape)
print(lin.weight.shape)

print('------------------------------')

# print(lin(torch.tensor( [ 1.0,  2.2,  4.3 ] )))
