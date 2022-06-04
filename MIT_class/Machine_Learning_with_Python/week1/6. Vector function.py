import numpy as np

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if (x>y):
        out = x/y
    else:
        out = x*y
    return out
    raise NotImplementedError

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    vectorized_arg = np.vectorize(scalar_function)
    vectorized_result = vectorized_arg(x, y)
    return vectorized_result
    
    raise NotImplementedError

a = np.array([1, 2])
b = np.array([3, 4])

result = vector_function(a, b)
print(result)