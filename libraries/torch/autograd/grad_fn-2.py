#!/usr/bin/env python

import torch
# import math

x_  = 3.1
a_  = 4.7
k_  = 3.0

x = torch.tensor([ x_ ], dtype=torch.double, requires_grad = True)
a = torch.tensor([ a_ ], dtype=torch.double, requires_grad = True)
k = torch.tensor([ k_ ], dtype=torch.double, requires_grad = True)

y = a * x ** k

d = 0.001
g = y.grad_fn( torch.tensor([ d ], dtype=torch.double))

print(g)


print( g[0].item() ) # 0.02979... =  d * x_ ** k_
print( g[1].item() ) # 0.0047     =  d * a_



print( d * x_ ** k_  )
print( d * a_        )


quit()
# print(g[0].grad_fn( torch.tensor([d]))  )
# print(g[1].grad_fn( torch.tensor([d]))  )
# print(y.grad_fn.next_function)

y.backward()

print(x.grad)
print(a.grad)
print(k.grad)

quit()

# y_ = a_ * x_ ** 3 

# yx = (x_+ d) **  n_
# yn =  x_     **( n_  + d)
# 
# print( yx - y_ )
# print( yn - y_ )
#  
# 
# 
# 
#  
# # gradients = y.grad_fn(torch.tensor([ d ]))
# # 
# # print(gradients[0])
# # print(gradients[1])
# # 
# # print(gradients[0].grad_fn( torch.tensor([ 2.0 ]) ))
# # print(gradients[1].grad_fn( torch.tensor([ 2.0 ]) ))
# # 
# # # 
# # # 
# # # # print(y.grad_fn(torch.tensor([ 2.0 ])))
# # # 
# # # # print(y.grad_fn(torch.tensor([1.0])))
# # # # print(dir(y.grad_fn))
