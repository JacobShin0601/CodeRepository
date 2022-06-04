import numpy as np

def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    sum = A + B
    s = np.linalg.norm(sum)

    return s

    raise NotImplementedError


A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
B = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18])

print(norm(A, B))