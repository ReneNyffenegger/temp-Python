import autograd.numpy as np
from autograd import grad

def hello_world(weights):
    weights = np.array(weights, dtype=np.float64)
    return np.dot(weights, np.array([1, 2, 3], dtype=np.float64))

gradient = grad(hello_world)
print(gradient(np.array([1, 1, 1], dtype=np.float64)))
