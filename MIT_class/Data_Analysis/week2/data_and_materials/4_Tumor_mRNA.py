import numpy as np
import pandas as pd
import scipy.stats as stats
import zipfile
import os

#print(os.getcwd())

with zipfile.ZipFile('MIT class/Data Analysis: Statistical Modeling and Computation/week2/statsreview_release1.zip') as zip_file:
    golub_data, golub_classnames = ( np.genfromtxt(zip_file.open('data_and_materials/golub_data/{}'.format(fname)), delimiter=',', names=True, converters={0: lambda s: int(s.strip(b'"'))}) for fname in ['golub.csv', 'golub_cl.csv'] )

print(golub_data)
print(golub_classnames)