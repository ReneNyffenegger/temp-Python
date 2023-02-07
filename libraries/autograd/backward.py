import autograd.numpy as np
from autograd import grad

def polynomial(coefficients, x):
    y = np.sum(coefficients * x**np.arange(len(coefficients)))
    return y

coefficients = np.array([2.0, 3.0, 4.0])
x = np.array([1.0, 2.0, 3.0])

gradient = grad(polynomial)(coefficients, x)

print(np.sum(gradient, axis=0))

