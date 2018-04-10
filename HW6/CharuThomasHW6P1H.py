import random
import numpy
import matplotlib.pyplot as plt

realizations = []

for i in range(1000):
	realizations.append(random.gauss(10,3))

plt.hist(realizations, bins='auto')
plt.show()