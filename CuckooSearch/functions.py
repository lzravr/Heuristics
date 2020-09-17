import numpy as np

def calculate(array, t):
    fitness = sphere(array)
    return fitness

def schwefel(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
    return fitness

def sphere(array):
    fitness = 0
    for i in range(len(array)):
        fitness = fitness + array[i]**2
    return fitness