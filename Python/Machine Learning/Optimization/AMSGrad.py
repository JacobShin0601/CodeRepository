
# example of plotting the amsgrad search on a contour plot of the test function
from math import sqrt
from numpy import asarray
from numpy import arange
from numpy.random import rand
from numpy.random import seed
from numpy import meshgrid
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
 
# objective function
def objective(x, y):
	return x**2.0 + y**2.0
 
# derivative of objective function
def derivative(x, y):
	return asarray([x * 2.0, y * 2.0])
 
# gradient descent algorithm with amsgrad
def amsgrad(objective, derivative, bounds, n_iter, alpha, beta1, beta2):
	solutions = list()
	# generate an initial point
	x = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# initialize moment vectors
	m = [0.0 for _ in range(bounds.shape[0])]
	v = [0.0 for _ in range(bounds.shape[0])]
	vhat = [0.0 for _ in range(bounds.shape[0])]
	# run the gradient descent
	for t in range(n_iter):
		# calculate gradient g(t)
		g = derivative(x[0], x[1])
		# update variables one at a time
		for i in range(x.shape[0]):
			# m(t) = beta1(t) * m(t-1) + (1 - beta1(t)) * g(t)
			m[i] = beta1**(t+1) * m[i] + (1.0 - beta1**(t+1)) * g[i]
			# v(t) = beta2 * v(t-1) + (1 - beta2) * g(t)^2
			v[i] = (beta2 * v[i]) + (1.0 - beta2) * g[i]**2
			# vhat(t) = max(vhat(t-1), v(t))
			vhat[i] = max(vhat[i], v[i])
			# x(t) = x(t-1) - alpha(t) * m(t) / sqrt(vhat(t)))
			x[i] = x[i] - alpha * m[i] / (sqrt(vhat[i]) + 1e-8)
		# evaluate candidate point
		score = objective(x[0], x[1])
		# keep track of all solutions
		solutions.append(x.copy())
		# report progress
		print('>%d f(%s) = %.5f' % (t, x, score))
	return solutions
 
# seed the pseudo random number generator
seed(1)
# define range for input
bounds = asarray([[-1.0, 1.0], [-1.0, 1.0]])
# define the total iterations
n_iter = 100
# steps size
alpha = 0.007
# factor for average gradient
beta1 = 0.9
# factor for average squared gradient
beta2 = 0.99
# perform the gradient descent search with amsgrad
solutions = amsgrad(objective, derivative, bounds, n_iter, alpha, beta1, beta2)
# sample input range uniformly at 0.1 increments
xaxis = arange(bounds[0,0], bounds[0,1], 0.1)
yaxis = arange(bounds[1,0], bounds[1,1], 0.1)
# create a mesh from the axis
x, y = meshgrid(xaxis, yaxis)
# compute targets
results = objective(x, y)
# create a filled contour plot with 50 levels and jet color scheme
pyplot.contourf(x, y, results, levels=50, cmap='jet')
# plot the sample as black circles
solutions = asarray(solutions)
pyplot.plot(solutions[:, 0], solutions[:, 1], '.-', color='w')
# show the plot
pyplot.show()