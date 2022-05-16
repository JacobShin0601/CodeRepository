import numpy as np

from numpy.random import default_rng
rng = default_rng()

n = 90000
results = np.array([])
for x in range(n):
    coin = rng.choice(["red","green","yellow"])
    coin_bias = 0.5 # green bias by default
    if(coin == "red"):
        coin_bias = 0.4
    if(coin == "yellow"):
        coin_bias = 0.6
    r = np.sum(rng.binomial(1,coin_bias,300))
    results = np.append(results,[r])
print("mean: " + str(np.mean(results)))
print("variance: " + str(np.var(results)))