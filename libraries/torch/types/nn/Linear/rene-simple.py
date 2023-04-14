import torch


lin = torch.nn.Linear(3, 2) # three inputs, two outputs



print(lin.bias  .shape)
print(lin.weight.shape)

print('------------------------------')

print(type(lin.bias  ))
print(type(lin.weight))

print('------------------------------')

# print(lin(torch.tensor( [ 1.0,  2.2,  4.3 ] )))
