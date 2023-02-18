#
#  https://www.geeksforgeeks.org/variables-and-autograd-in-pytorch/
#
import torch
from torch.autograd import Variable
  
# packing the tensors with Variable
a = Variable(torch.tensor([5., 4.]), requires_grad=True)
b = Variable(torch.tensor([6., 8.]))
  
# polynomial function with a,b as variable
y = ((a**2)+(5*b))
z = y.mean()
  
# dy/da=2*a=10,8
# dy/db=5
  
# computing gradient
z.backward()
  
# printing out
print('Gradient of a', a.grad)
print('Gradient of b', b.grad)
