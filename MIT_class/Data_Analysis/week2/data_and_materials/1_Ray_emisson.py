import numpy as np
import pandas as pd
import scipy.stats as stats


df = pd.read_csv('MIT_class/Data_Analysis/week2/data_and_materials/gamma-ray.csv', ',', decimal='.')
df = df.round(4)
pd.set_option('display.float_format', '{:.4f}'.format)

df_new = df.astype(np.float)
print(df_new)

#print(df_new.mean(axis=0))

# significance level
alpha = 0.05





