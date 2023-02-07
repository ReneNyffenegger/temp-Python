import autograd.numpy as np
from autograd import grad

def hello_world(weights):
    return np.dot(weights, np.array([1, 2, 3]))

gradient = grad(hello_world)
print(gradient(np.array([1, 1, 1])))

# ==> TypeError: Can't differentiate w.r.t. type <class 'numpy.int32'>
#
#
# The error message you're encountering is because the grad function from
# Autograd can only differentiate functions that take in arrays or tensors of
# floating-point numbers. In this case, it seems like the input to hello_world
# is of type numpy.int32, which is not a supported type.
#
# To fix this issue, you can simply convert the input to a floating-point type,
# such as numpy.float64:
