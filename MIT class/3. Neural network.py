import numpy as np

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    weights_T = np.transpose(weights)
    out_x = np.matmul(weights_T, inputs)
    #print(out_x)
    out = np.tanh(out_x)
    return out
    raise NotImplementedError

X = np.array([[3], [2]])
Y = np.array([[7], [8]])
result = neural_network(X, Y)

shape = np.shape(result)

print(result)