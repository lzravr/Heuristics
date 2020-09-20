# Kod prostog Cuckoo Search algoritma ne postoji ralika izmedju
# gnezda, jajeta i kukavice, kako jedno gnezno odgovara jednom
# jajetu koje je polozila jedna kukavica. Ova klasa predsavlja 
# zapravo jedno resenje. A zvacemo je kukavica.

import numpy as np
import math
import functions as fn
from cs_parameters import Params as params


def levy_flight(la):
    # generisanje koraka levijevom raspodelom
    sigma1 = np.power((math.gamma(1 + la) * np.sin(np.pi * la / 2)) / (la * math.gamma((1 + la) / 2) * np.power(2, (la - 1) / 2)), 1 / la )
    sigma2 = 1

    u = np.random.normal(0, sigma1, size=params.get_dimension())
    v = np.random.normal(0, sigma2, size=params.get_dimension())

    step = u / np.power(np.fabs(v), 1 / la)

    # vraca n-dimenzioni vektor koordinata (n - params.get_dimension())
    return step


class Cuckoo:
    def __init__(self):
        self.position = np.random.rand(params.get_dimension()) * (params.get_domain_max() - params.get_domain_min()) + params.get_domain_min()
        self.fitness = fn.calculate(self.position)
    
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, fitness):
        self.fitness = fitness

    def abandon(self):
        # odbacujemo resenje i ujedno generisemo novo (menjamo udeo pa koordinata vektora pozicije)
        for i in range(len(self.position)):
            p = np.random.rand()
            if p < params.get_pa():
                self.position[i] = np.random.rand() * (params.get_domain_max() - params.get_domain_min()) + params.get_domain_min()
    
    def move_cuckoo(self):
        step = params.get_step_size() * levy_flight(params.get_lambda())

        # pomeranje kukavice
        self.position = self.position + step

        # provera da li je izasla iz prostora pretrage
        for i in range(len(self.position)):
            if self.position[i] > params.get_domain_max():
                self.position[i] = params.get_domain_max()
            if self.position[i] < params.get_domain_min():
                self.position[i] = params.get_domain_min()

    def print_cuckoo(self):
        print("fitness:",str(self.fitness).rjust(14," "),
              "\nposition:",np.round(self.position,decimals=4))
