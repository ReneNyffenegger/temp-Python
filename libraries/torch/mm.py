import sys
import torch




m1 = torch.tensor([

  [ 0.9, 1.3 ],
  [ 4.2, 5.2 ],
  [ 2.1, 3.0 ]
 
])

sys.exit()





# ---------------------------














lin = torch.nn.Linear(3, 2) # three inputs, two outputs

# print(lin.bias  .shape)    # torch.Size([2])     = number of outputs
# print(lin.weight.shape)    # torch.Size([2, 3])  = number of outputs x number of inputs


x_0 = 1.0
x_1 = 2.2
x_2 = 0.9

x_tensor = torch.tensor([ x_0, x_1, x_2 ])

print( x_tensor @ lin.weight.t() + lin.bias )
print( x_tensor.matmul(lin.weight.t()) + lin.bias )
print( torch.matmul(x_tensor, lin.weight.t()) + lin.bias )

print(lin( x_tensor ))




print('------------------------------')

# print(type(lin.bias  ))
# print(type(lin.weight))

w_0_0 = lin.weight[0, 0].item()
w_1_0 = lin.weight[1, 0].item()
w_0_1 = lin.weight[0, 1].item()
w_1_1 = lin.weight[1, 1].item()
w_0_2 = lin.weight[0, 2].item()
w_1_2 = lin.weight[1, 2].item()

b_0   = lin.bias[0].item()
b_1   = lin.bias[1].item()


d_0 = x_0 * w_0_0 + \
      x_1 * w_0_1 + \
      x_2 * w_0_2

d_1 = x_0 * w_1_0 + \
      x_1 * w_1_1 + \
      x_2 * w_1_2


r_0 = d_0 + b_0
r_1 = d_1 + b_1

print(f'r_0 = {r_0}, r_1 = {r_1}')

