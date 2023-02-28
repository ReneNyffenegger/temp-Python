#!/usr/bin/env python

import torch
# import math


def calc(a, x, k):
    return a * x ** k


def print_graph(g, level=0):
 #
 #  https://stackoverflow.com/a/51814367/180275
 #
    if g == None: return
    print(' -' * level*2, g)
    for subg in g.next_functions:
        print_graph(subg[0], level+1)



x_  = 3.1
a_  = 4.7
k_  = 3.0

x   = torch.tensor([ x_ ], dtype=torch.double, requires_grad = True)
a   = torch.tensor([ a_ ], dtype=torch.double, requires_grad = True)
k   = torch.tensor([ k_ ], dtype=torch.double, requires_grad = True)

d   = 0.0001

y   = calc(a   , x   , k )

print_graph(y.grad_fn)


print(type(y.grad_fn))
print(dir(y.grad_fn))


quit()


y_  = calc(a_  , x_  , k_)

yda = calc(a_+d, x_  , k_  )
ydx = calc(a_  , x_+d, k_  )
ydk = calc(a_  , x_  , k_+d)

# y = a * x ** k
# y_= a_* x_** k_
# 
# ya==(a_+d


g = y.grad_fn( torch.tensor([ d ], dtype=torch.double))

# print_graph(g[0].grad_fn)

print(g)


print(  yda-y_ )
print( g[0].item() ) # 0.02979... =  d * x_ ** k_
print()
print(  ydx-y_ )
print( g[1].item() ) # 0.0047     =  d * a_
print()
print(  ydk-y_ )


quit()


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
