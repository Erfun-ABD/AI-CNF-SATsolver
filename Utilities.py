import random, math

def countTrueClauses(clauses, variables):
    count = 0
    for clause in clauses:
        for literal in clause:
            if literal == variables[abs(literal) - 1]:
                count += 1
                break
    return count



def simulatedAnnealing(clauses, varNum, T = 10000, Tmin = 0.00001, Alpha = 0.998):
    variables = [(random.choice([-1, 1]) * i) for i in range(1, varNum+1)]


    E = countTrueClauses(clauses, variables)
    Eth = len(clauses)

    Elist = [E]
    Tlist = [T]

    while (T > Tmin and E < Eth):
        randIndex = random.randint(0, varNum-1)

        newVariables = variables.copy()
        newVariables[randIndex] = -newVariables[randIndex]

        newE = countTrueClauses(clauses, newVariables)

        if (simulatedAnnealingAccept(newE - E, T)):
            variables = newVariables
            E = newE
            Elist.append(E)
            Tlist.append(T)

        T *= Alpha

    print("SimulatedAnnealing  " + "T: " + str(Tlist[0]), "Alpha: " + str(Alpha))

    return variables, Elist, Tlist

def simulatedAnnealingAccept(deltaE, T):
    if deltaE > 0:
        return True
    else:
        return random.random() < math.exp(-abs(deltaE)/T)



 
def genetic(clauses, varNum, MaxIteration = 2000, PopulationSize = 10, Pc = 0.8, Pm = 0.1):
    population = {}

    while len(population) < PopulationSize:
        variables = [(random.choice([-1, 1]) * i) for i in range(1, varNum+1)]
        E = countTrueClauses(clauses, variables)
        population[tuple(variables)] = E

    population = dict(sorted(population.items(), key=lambda item: item[1], reverse=True))
    
    Emax = list(population.values())[0]
    Eth = len(clauses)
    Elist = [Emax]

    Divlist = [list(population.values())]

    iteration = 0
    while (iteration < MaxIteration and Emax < Eth):
        newPopulation = {}

        for i in range(PopulationSize//2):
            parents = random.choices(list(population.keys()),
                            range(1, PopulationSize+1),
                            k = 2)

            child1, child2 = crossOver(parents[0], parents[1], Pc)

            child1 = Mutation(child1, Pm)
            child2 = Mutation(child2, Pm)

            E1 = countTrueClauses(clauses, child1)
            E2 = countTrueClauses(clauses, child2)

            newPopulation[child1] = E1
            newPopulation[child2] = E2

        newPopulation.update(population)

        population = dict(sorted(newPopulation.items(), 
                            key=lambda item: item[1], reverse=True)[:PopulationSize])
        
        
        Emax = list(population.values())[0]
        Elist.append(Emax)

        Divlist.append(list(population.values()))

        iteration += 1

    print("Genetic  " + "MaxIteration: " + str(MaxIteration),
            "PopulationSize: " + str(PopulationSize),
            "Pc: " + str(Pc), "Pm: " + str(Pm))

    variables = list(list(population.keys())[0])

    return variables, Elist, Divlist


def crossOver(parent1, parent2, Pc):
    randIndex = random.randint(0, len(parent1)-1)

    child1 = list(parent1).copy()
    child2 = list(parent2).copy()

    if random.random() < Pc:
        child1 = list(parent1[:randIndex] + parent2[randIndex:])
        child2 = list(parent2[:randIndex] + parent1[randIndex:])

    return child1, child2

def Mutation(parent, Pm):
    randIndex = random.randint(0, len(parent)-1)

    child = parent.copy()
    
    if random.random() < Pm:
        child[randIndex] = -child[randIndex]

    return tuple(child)

