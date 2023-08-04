from pysat.formula import CNF

from functools import reduce
import matplotlib.pyplot as plt
import random, math

import Utilities as ut


formula = CNF(from_file="Inputs/Input.cnf")
# formula = CNF(from_file="Inputs/UInput.cnf")


fig1, axs1 = plt.subplots(2, 1)

variables, Elist, Tlist = ut.simulatedAnnealing(formula.clauses, formula.nv)

print("True clauses: " + str(Elist[-1]))
print("variables: " + str(variables))

axs1[0].scatter(Tlist, Elist, s=0.3)
axs1[0].plot(Tlist, Elist, linewidth=0.1, color='r')
axs1[0].set_xscale('log')
axs1[0].set_xlim(Tlist[0]*2, Tlist[-1]/2)

variables, Elist, Divlist = ut.genetic(formula.clauses, formula.nv)

print("True clauses: " + str(Elist[-1]))
print("variables: " + str(variables))

axs1[1].scatter(range(2000+1), Elist, s=0.3)
axs1[1].plot(range(2000+1), Elist, linewidth=0.2, color='r')



# fig2, axs2 = plt.subplots(2, 2)
# t=1
# for i in range(2):
#     for j in range(2):
#         variables, Elist, Tlist= ut.simulatedAnnealing(formula.clauses, formula.nv, T = t)
        
#         axs2[i,j].scatter(Tlist, Elist, s=0.3)
#         axs2[i,j].plot(Tlist, Elist, linewidth=0.1, color='r')
#         axs2[i,j].set_xscale('log')
#         axs2[i,j].set_xlim(Tlist[0]*2, Tlist[-1]/2)
#         t *= 10


# fig3, axs3 = plt.subplots(2, 2)

# t=2
# for i in range(2):
#     for j in range(2):
#         variables, Elist, Divlist= ut.genetic(formula.clauses, formula.nv, PopulationSize=t)
        
#         axs3[i,j].scatter(range(2000+1), Elist, s=0.3)
#         axs3[i,j].plot(range(2000+1), Elist, linewidth=0.2, color='r')
#         t *= 10


# fig4, axs4 = plt.subplots(2, 2)
# maxIt=2
# for i in range(2):
#     for j in range(2):
#         variables, Elist, Divlist= ut.genetic(formula.clauses, formula.nv, MaxIteration=maxIt)
        
#         axs4[i,j].scatter(list(map(lambda x: [x]*10, range(maxIt+1))), list(reduce(lambda a,b:a+b, Divlist)), s=0.3)
#         axs4[i,j].plot(range(maxIt+1), list(map(lambda x: x[0], Divlist)), linewidth=0.2, color='r')
        # maxIt *= 10

plt.show()