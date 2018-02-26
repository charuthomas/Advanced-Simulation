"""
This module is a simulation of a Moving Average Process. For more information, read up on Stationary
Stochastic Processes and/or Time Series Regression. The Moving Average model is well documented
and the theoretical reasons this model makes sense can be shown in some proofs (not necessarily simple)

Examples:
	Run script (assuming necessary dependencies) with
		$ python HW3Problem5.py

	Trials from generatePath are printed with both individual observations and summary stats 
	on observations
		0: ...
		1: ...
		...
		xbar: ...
		sd: ...
		...
"""
import numpy, scipy.stats, statistics, math

xbars = []
sns = []
cis = []
ci_alts = []

t_critical = scipy.stats.t.ppf(0.95,9999)
z_critical = scipy.stats.norm.ppf(0.95)
mu = 5
sigma = math.sqrt(36)

def generatePath(mean, sd, n, q):
	"""
	This function generates one path from the MA process xi = 5 + et + 2/3 et-1 + 1/3 et-2,
	a dampened moving average process
	Errors are distributed according to a normal distribution with mean and sd from args

	Args:
		mean: mean of errors, normal distribution
		sd: sd of errors, normal distribution
		n: number of observations or length of path
		q: lag of moving average process

	Returns:
		none: fruitless function, may change later
	"""
	errors = numpy.random.normal(mean, sd, n+q)
	xi = []
	for i in range(n):
		xi.append(5 + errors[i+q]+ 2/3*errors[i+q-1] + 1/3*errors[i+q-2])
		#print(str(i) + ": " + str(xi[i]))

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
	This function runs repeated replications of a particular MA process generated

	Args:
		numReps: number of replications for experiment
		mean: mean of errors, normal distribution
		sd: sd of errors, normal distribution
		n: number of observations or length of single path
		q: lag of moving average process

	Returns:
		none: fruitless function, may change later
	"""
	for i in range(numReps):
		generatePath(mean,sd,n,q)

def checkWithinInterval(intervalTups, numReps, mean=0):
	"""
	This function checks the fraction of confidence intervals, represented as tuples,
	which contain the mean of the MA process

	Args:
		intervalTups: array of confidence intervals, likely generated from multiple replications
		numReps: number of replications for experiment
		mean: theoretical mean of MA process, usually the constant before the error terms; default 0

	Returns:
		meanFraction: float representing number of CIs that contain mean
	"""
	i = 0
	for interval in intervalTups:
		if interval[0] <= mean <= interval[1]:
			i += 1

	meanFraction = i / numReps
	return meanFraction

runReplications(400, 0, 3, 10000, 3)
cisWithin = checkWithinInterval(cis, 400, mu)
ci_altsWithin = checkWithinInterval(ci_alts, 400, mu)

#TEST CASE: 3 replications, length of 5 on each path
# runReplications(3, 0, 3, 5, 3)
# cisWithin = checkWithinInterval(cis, 3, mu)
# ci_altsWithin = checkWithinInterval(ci_alts, 3, mu)

print(cisWithin)
print(ci_altsWithin)