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

x = 3
y = 7

result = scalar_function(x, y)
print(result)