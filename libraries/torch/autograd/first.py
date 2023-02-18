import torch
# from random import random

x        = torch.tensor([ 1.3 , 2.9, 4.2, 5.8 ], dtype = torch.float32, requires_grad = True)
expected = torch.tensor([ 4.5 ,-1.7, 3.6, 2.3 ], dtype = torch.float32)

#a        = torch.rand(1) ; a.requires_grad = True # random()
#b        = torch.rand(1) ; b.requires_grad = True # random()
#c        = torch.rand(1) ; c.requires_grad = True # random()
#d        = torch.rand(1) ; d.requires_grad = True # random()

a        = torch.rand(1, requires_grad = True)
b        = torch.rand(1, requires_grad = True)
c        = torch.rand(1, requires_grad = True)
d        = torch.rand(1, requires_grad = True)

for i in range(10000):

    y = a * x**3 + \
        b * x**2 + \
        c * x**1 + \
        d * x**0
    
    loss = (y-expected).pow(2).sum()
    loss_ = loss.item()
    print('loss = ' + str(loss_))
    loss.backward()
    with torch.no_grad():
    #    print(f'y = {y.item()} a = {a.item()}, b = {b.item()}')
      #
      #  torch.no_grad() temporarily sets all of the requires_grad
      #  flags to false.
      #  This is used here to prevent torch from calculating the
      #  gradients when updating their values:
      #
      #  We use in-place subtraction ( a -= …) rather than
      #  explicit subtraction ( a = a - … ) so as not to
      #  loose the variables' internal property requires_grad = True
      #  See this stackoverflow answer for more information:
      #     https://stackoverflow.com/a/72786882
      #

         learning_rate = 1e-6
      #  learning_rate = loss_ / 10000000
         a -= learning_rate * a.grad
         b -= learning_rate * b.grad
         c -= learning_rate * c.grad
         d -= learning_rate * d.grad

    a.grad.zero_()
    b.grad.zero_()
    c.grad.zero_()
    d.grad.zero_()

    # print(a.grad)
    # print(type(y))
    
    #n  = torch.tensor([   2 ,   3 ,   1 ])
    
    #in * n:e
