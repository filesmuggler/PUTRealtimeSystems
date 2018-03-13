import math
import matplotlib.pyplot as plt
import pylab

C = [5, 1, 4]
D = [16, 3, 7]
T = [18, 3, 9]

hyperperiod = 18

results = []

for t in range(hyperperiod):
    Cp1 = C[0] * (math.floor(((t-D[0])/T[0]))+1)
    Cp2 = C[1] * (math.floor(((t-D[1])/T[1]))+1)
    Cp3 = C[2] * (math.floor(((t-D[2])/T[2]))+1)
    Cs = Cp1 + Cp2 + Cp3
    results.append(Cs)

graph = plt.figure()
ax1 = graph.add_subplot(121)
ax1.plot(range(hyperperiod),range(hyperperiod),'b-',label='CPU[s]')
ax1.step(range(hyperperiod),results, 'r-', label='TDF[s]')
pylab.legend(loc='upper left')


C = [1, 1, 1]
D = [7, 12, 6]
T = [7, 14, 7]

hyperperiod = 18

results = []

for t in range(hyperperiod):
    Cp1 = C[0] * (math.floor(((t-D[0])/T[0]))+1)
    Cp2 = C[1] * (math.floor(((t-D[1])/T[1]))+1)
    Cp3 = C[2] * (math.floor(((t-D[2])/T[2]))+1)
    Cs = Cp1 + Cp2 + Cp3
    results.append(Cs)


ax2 = graph.add_subplot(122)
ax2.plot(range(hyperperiod),range(hyperperiod),'b-',label='CPU[s]')
ax2.step(range(hyperperiod),results, 'r-', label='TDF[s]')
pylab.legend(loc='upper left')

plt.show()
