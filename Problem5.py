import numpy, scipy.stats, statistics, math

xbars = []
sns = []
cis = []
ci_alts = []

t_critical = scipy.stats.t.ppf(0.95,9999)
z_critical = scipy.stats.norm.ppf(0.95)
mu = 5
sigma = 2 #CHANGE TO CORRECT VALUE OF SIGMA

def generatePath(mean, sd, n, q):
	"""
	"""
	errors = numpy.random.normal(mean, sd, n+q)
	xi = []
	for i in range(n):
		xi.append(5 + errors[i+q]+ 2/3*errors[i+q-1] + 1/3*errors[i+q-2])
		print(str(i) + ": " + str(xi[i]))

	xbar = sum(xi) / float(len(xi))
	sn = statistics.stdev(xi)
	ci = (xbar - t_critical*sn/math.sqrt(n), xbar + t_critical*sn/math.sqrt(n))
	ci_alt = (xbar - z_critical*sigma/math.sqrt(n), xbar + z_critical*sigma/math.sqrt(n))

	xbars.append(xbar)
	sns.append(sn)
	cis.append(ci)
	ci_alts.append(ci_alt)
	print("xbar: " + str(xbar))
	print("sd: " + str(sn))
	print("ci: " + str(ci))
	print("ci alt: " + str(ci_alt))

def runReplications(numReps, mean, sd, n, q):
	"""
	"""
	for i in range(numReps):
		generatePath(mean,sd,n,q)

def checkWithinInterval(intervalTups, mean):
	"""
	"""


#runReplications(400, 0, 3, 10000, 3)

generatePath(0,3,5,3)