#!/usr/bin/env python

import torch
import math

x_  = 3.1
a_  = 4.7


x = torch.tensor([ x_ ], dtype=torch.double, requires_grad = True)
a = torch.tensor([ a_ ], dtype=torch.double, requires_grad = True)



#print(y.grad_fn( torch.tensor(1.0) ))
#print(y.grad_fn( torch.tensor(1.0))[0])
#print(y.grad_fn( torch.tensor(1.0))[1])
#
#print( (a_+1) * x_ ** 2)
#print( (a_  ) * (x_+1) ** 2)
#
#quit()

y  = a  ** x #  ** 3
y_ = a_ ** x_#  ** 3


print('grad fn''s')
print(x.grad_fn)
print(a.grad_fn)
print(y.grad_fn)
print('')

d  = 0.001


g = y.grad_fn( torch.tensor([ d ], dtype=torch.double))

print( g[0].item() )
print( g[1].item() )

print( ( x_ * a_ ** (x_-1) ) * d)
print( (      a_ ** (x_  ) * math.log(a_) * d))

quit()

# print(a.grad_fn( torch.tensor([ d ]) ))

yx =  a_      ** (x_+d) # **  3
ya = (a_ + d) **  x_    # **  3



print( (ya - y_)  )
print( (yx - y_)  )

quit()


y.backward()

print(x.grad) # 135.5010 = a * 3*x**2
print(a.grad) #  29.7910 = x**3

# Kind of important:
#
# x.grad.zero_()
# a.grad.zero_()

y = a * x ** 3

y.backward()

print(x.grad)
print(a.grad)


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
