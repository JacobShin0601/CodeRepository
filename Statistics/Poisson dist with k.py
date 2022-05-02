import matplotlib.pyplot as plt
from scipy.stats import expon

k_arrivals = [1, 5, 25, 100]  # Number of k arrivals at time Yk             
n = 10000                     # Number of trials/experiments
distribution = expon(scale=1/1)     # Exponential distribution, λ = 1 (scale = 1/λ)

# Setup axes for plotting
fig, ax = plt.subplots(figsize=(12, 8), nrows=2, ncols=2)
ax = ax.flatten()

for i, k in enumerate(k_arrivals):

    # Draw underlying RVs. Each row is a simulation with columns representing the ith arrival, up to kth inter-arrival time
    data = distribution.rvs((n,k))

    # To get the time to k arrivals, we sum across the columns for each trial for Y_k
    Y_k = data.sum(axis=1)

    # Plot the distribution to k arrivals
    ax[i].hist(Y_k, bins=60, alpha=0.5, density=True)
    ax[i].set_title(f"Time to k = {k} arrivals, n = {n}")

plt.show()