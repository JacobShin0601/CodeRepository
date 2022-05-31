import matplotlib.pyplot as plt # import the library
plt.scatter(Xs, Ys) # Create the scatter plot, Xs and Ys are two numpy arrays of the same length
plt.show() # Display the plot you just created.

plt.plot(Xs, Ys)

import numpy as np
np.linalg.inv(matrix_to_invert)
# This will draw a line through the X, Y pairs defined by the Xs and Ys numpy arrays.

# When working with matrices, numpy provides some convenient facilities. For example, to find the inverse of a matrix, use



##The scipy package provides statistical distributions. For example, to calculate p-values for the t-distribution, you can use the survival function (sf):
import scipy.stats
scipy.stats.t.sf(T, num_degrees_of_freedom)