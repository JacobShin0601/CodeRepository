#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from sklearn.datasets import fetch_olivetti_faces
from ipywidgets import interact
image_shape = (64, 64)
# Load faces data
dataset = fetch_olivetti_faces(data_home='./')
faces = dataset.data

plt.figure(figsize=(10,10))
plt.imshow(np.hstack(faces[:5].reshape(5,64,64)), cmap='gray');

# for numerical reasons we normalize the dataset
mean = faces.mean(axis=0)
std = faces.std(axis=0)
faces_normalized = (faces - mean) / std

#B = np.load('eigenfaces.npy')[:50] # we use the first 50 basis vectors --- you should play around with this.
#print("the eigenfaces have shape {}".format(B.shape))
#
##plt.figure(figsize=(10,10))
##plt.imshow(np.hstack(B[:5].reshape(-1, 64, 64)), cmap='gray');

@interact(i=(0, 10))
def show_face_face_reconstruction(i):
	original_face = faces_normalized[i].reshape(64, 64)
	# reshape the data we loaded in variable `B` 
	B_basis = B.reshape(B.shape[0], -1).T
	face_reconstruction = project_general(faces_normalized[i], B_basis).reshape(64, 64)
	plt.figure()
	plt.imshow(np.hstack([original_face, face_reconstruction]), cmap='gray')
	plt.show()
	
	