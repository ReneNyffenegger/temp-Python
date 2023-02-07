import autograd.numpy as np
from autograd import grad

def f(x, a, b, c):
    return a * x**2 + b * x + c

gradient = grad(f)
x = np.array(2.0)
a = np.array(3.0)
b = np.array(4.0)
c = np.array(5.0)
print(gradient(x, a, b, c))
