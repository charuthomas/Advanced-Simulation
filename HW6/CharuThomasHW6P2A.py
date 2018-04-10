import random
import math
import numpy as np 
import pylab 
import scipy.stats as stats

"""GENERATE CUTPOINTS
"""
pdf = {1: 0.029, 2: 0.039, 3: 0.03, 4:.131, 5:.083, 6:.049, 7:.127, 8:.012, 9:0.032, 10:0.04, 11:0.029, 12:0.028, 13:0.043, 14:0.012,15:.128, 16:0.061, 17:0.027, 18:.1}
cdf = {}
cumsum = 0

for i in pdf:
	cdf[i] = cumsum + pdf[i]
	cumsum += pdf[i]

j = 0
k = 0
A = 0
m = 18
cutpoints = {}

while j < m:
	while A <= j:
		k = k + 1
		A = m*cdf[k]
	j = j + 1

	cutpoints[j] = k

print(cutpoints)

"""ALGORITHM CM SAMPLE GENERATION
"""
sample = []

for i in range(10000):
	U = random.uniform(0,1)
	L = math.floor(m*U) + 1
	X = cutpoints[L]
	while U > cdf[X]:
		X = X + 1

	sample.append(X)

"""EVALUATE CORRECTNESS OF SAMPLE CDF
"""
stats.probplot(sample, plot=pylab)
pylab.show()
