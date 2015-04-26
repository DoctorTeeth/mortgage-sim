from simulator import runSimulation, runMany

N = 120
p = 0.01
d = 0.01

dic = runSimulation(N,p,d)

str1 = "using a prepay rate of " + str(p)
str2 = " and a default rate of " + str(d)

print str1 + str2

print dic['x']

print dic['y']

runMany(120)
