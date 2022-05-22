from termios import NL1
import numpy as np
import scipy
from scipy import stats


table = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3.0, 2.7, 0.6, 3.6, -0.5])

result, p_value = scipy.stats.ttest_1samp(table, 0)
print(result, p_value)
p_value = p_value/2