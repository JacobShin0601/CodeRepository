import numpy as np
import pandas as pd
import scipy.stats as stats
import zipfile
import os

def add_intercept(X):
  return np.concatenate((np.ones_like(X[:]), X), axis=1)

def gradient_descent(gradient, start, learn_rate, tolerance=1e-06
):
    vector = start
    rows, cols = gradient.shape
    for _ in range(rows):
        diff = -learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector

Xs = pd.read_csv('MIT_class/Data_Analysis/week2/data_and_materials/syn_X.csv', header=None, decimal='.')
Ys = pd.read_csv('MIT_class/Data_Analysis/week2/data_and_materials/syn_X.csv', header=None, decimal='.')

print(Xs)
#print(np.ones_like(Xs[:]))

#Xs_T = Xs.T
Xs_new = add_intercept(Xs)
Xs_new = np.delete(Xs_new, 1, 1)
print(Xs_new)

#Xs = Xs.T
betaVec = np.linalg.inv(Xs_new.T.dot(Xs_new)).dot(Xs_new.T).dot(Ys)
print(betaVec)

#gradient_descent_temp = gradient_descent(betaVec, Ys, 0.05)
#print(gradient_descent_temp)


Ys_new = add_intercept(Ys)
print(Ys_new)