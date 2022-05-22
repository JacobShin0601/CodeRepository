import scipy
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import fisher_exact
from scipy.stats import norm

n = int(31000)
case = int(63)
p = float(case/n)

comb = scipy.special.comb(n, case)
result = comb*(p**case)*(1-p)**(n-case)

print(result)


### binomial distribution significance test
result2 = scipy.stats.binom.ppf(0.05, 31000, 0.00203)
print(result2)

### binomial distribution P values##
result3 = scipy.stats.binom_test(39, n=31000, p=0.00203, alternative='less')
print(result3)

## fisher exact test - P values##
table = [[39, 30961], [63, 30937]]
#table = [[39, 63], [30961, 30937]]
oddsr, p = fisher_exact(table, alternative='less')
print(p)

## Z-test with 
n = 31000
case_real = 39
x_bar = case_real/n
case_hypothesized = 63
pi = case_hypothesized/n
sigma = (pi*(1-pi))**(1/2)

z = (x_bar - pi)/(sigma/(n)**(1/2))

p_value = norm.cdf(z, loc=0, scale=1)
print(p_value)


##Likelihood ration test
#-2*math.log(binom.pmf(39,31000,102/62000) * binom.pmf(63,31000,102/62000) / (binom.pmf(39,31000,39/31000) * binom.