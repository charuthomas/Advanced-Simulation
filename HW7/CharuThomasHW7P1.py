import statistics

fh = open('hw6_Experiment1_Scenario1_Rep1.dat', 'r')

lines = fh.readlines()
floatLines = []

total = 0

for line in lines:
	total = total + float(line)
	floatLines.append(float(line))

xbar = total/len(lines)
sd = statistics.stdev(floatLines)
ci = (xbar - 1.96*sd/len(lines), xbar + 1.96*sd/len(lines))

print(xbar)
print(sd)
print(ci)