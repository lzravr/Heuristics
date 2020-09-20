import numpy as np
from cuckoo import Cuckoo
import functions as fn
import os
import sys
import csv
from cs_parameters import Params as params
import time

if os.path.exists("results"):
    pass
else:
    os.mkdir("results")

results = open("results" + os.sep + "results.csv", "w")
results_writer = csv.writer(results, lineterminator="\n")

def main():
    np.random.seed(round(time.time()))

    cuckoos = []

    # Generisanje populacije
    for p in range(params.get_population_size()):
        cuckoos.append(Cuckoo())

    cuckoos = sorted(cuckoos, key=lambda cuckoo: cuckoo.get_fitness())

    best_position = cuckoos[0].get_position()
    best_fitness = cuckoos[0].get_fitness()

    for iteration in range(params.get_iterations()):

        #generisanje novih resenja
        for i in range(len(cuckoos)):

            cuckoos[i].move_cuckoo()
            cuckoos[i].set_fitness(fn.calculate(cuckoos[i].get_position()))

            # nasumicno biramo resenje sa kojim uporedjujemo novo generisano
            j = np.random.randint(0, params.get_population_size())
            while j == i:
                j = np.random.randint(0, params.get_population_size())

            # za probleme minimizacije
            if (cuckoos[i].get_fitness() < cuckoos[j].get_fitness()):
                cuckoos[j].set_position(cuckoos[i].get_position())
                cuckoos[j].set_fitness(cuckoos[i].get_fitness())
        
        cuckoos = sorted(cuckoos, key=lambda cuckoo: cuckoo.get_fitness())

        # zadrzavamo najbolje resenje
        for a in range(1, len(cuckoos)):
            r = np.random.rand()
            if ( r < params.get_pa() ):
                cuckoos[a].abandon()
                cuckoos[a].set_fitness(fn.calculate(cuckoos[a].get_position()))
        
        cuckoos = sorted(cuckoos, key=lambda cuckoo: cuckoo.get_fitness())

        if ( cuckoos[0].get_fitness() < best_fitness ):
            best_fitness = cuckoos[0].get_fitness()
            best_position = cuckoos[0].get_position()

        sys.stdout.write("\r Iteration:%7d, BestFitness:%.4f" % (iteration, best_fitness))
        print()
        print(best_position)
    
        results.write(str(iteration) + "," + str(best_fitness) + "\n")

    results.close()
    input()
            

main()