import torch
# from random import random

x        = torch.tensor([ 1.3 , 2.9, 4.2, 5.8 ], requires_grad = True)
expected = torch.tensor([ 4.5 ,-1.7, 3.6, 2.3 ])

a        = torch.rand(1) ; a.requires_grad = True # random()
b        = torch.rand(1) ; a.requires_grad = True # random()
c        = torch.rand(1) ; a.requires_grad = True # random()
d        = torch.rand(1) ; a.requires_grad = True # random()


for i in range(100):

    y = a * x**3 + \
        b * x**2 + \
        c * x**1 + \
        d
    
    loss = (y-expected).pow(2).sum()
    loss_ = loss.item()
    print(loss_)
    loss.backward()


    a = a - loss_ / 100 * a.grad
    b = b - loss_ / 100 * b.grad
    c = c - loss_ / 100 * c.grad
    d = d - loss_ / 100 * d.grad



    
    # print(a.grad)
    # print(type(y))
    
    #n  = torch.tensor([   2 ,   3 ,   1 ])
    
    #in * n:e
