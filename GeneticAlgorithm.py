# name, calories, protein, carb, fat, price for each 100g
import random
from datetime import datetime

random.seed(datetime.now())

# 100g of each fooodstuff, with their respective nutritional value and price
foods = [
    ['corn', 60, 4, 5, 3, 2.5],
    ['rice', 39, 3, 7, 1, 0.7],
    ['lettuce', 20, 2, 2, 0.5, 1.1],
    ['hay', 76, 5, 10, 2, 2.2],
    ['grass', 15, 1.375, 1.375, 0.5, 0.9],
    ['grain', 24, 2, 3, 0.5, 1.4]
]

numberOfGenerations = 100


def generatePopulation(size):
    population = []
    score = 0
    for i in range(size):
        cornProb = random.randint(0, 1)
        riceProb = random.randint(0, 1)
        lettuceProb = random.randint(0, 1)
        hayProb = random.randint(0, 1)
        grassProb = random.randint(0, 1)
        grainProb = random.randint(0, 1)
        new = [cornProb, riceProb, lettuceProb, hayProb, grassProb, grainProb]
        population.append(new)
    return population


def mutation(offspring):
    for i in range(len(offspring)):
        prob = random.uniform(0.0, 1.0)
        if prob < 0.05:
            if offspring[i] == 1:
                offspring[i] = 0
            else:
                offspring[i] = 1
    return offspring


def populationFitness(population, funds):
    fitness = 0
    for i in range(len(population)):
        fitness += calculateFitness(population[i], funds)
    return fitness


def calculateFitness(solution, funds):
    score = 0
    totalPrice = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            score += foods[i][1]
            totalPrice += foods[i][5]
    if totalPrice > funds:
        score = 0
    return score


def selection(population, funds):
    return random.choices(
        population=population,
        weights=[calculateFitness(population[i], funds) for i in range(len(population))],
        k=2
    )


def middlePointCrossover(parents):
    offspring1 = parents[0][0:3] + parents[1][3:6]
    offspring2 = parents[1][0:3] + parents[0][3:6]

    return offspring1, offspring2


def formatResult(array, funds):
    formattedArray = []
    print(array)
    for i in range(len(array)):
        if array[i] == 1:
            formattedArray.append(foods[i][0])
    score = calculateFitness(array, funds)
    print("Score of best solution: " + str(score))
    print("Solution composed of: ")
    for i in range(len(array)):
        print(formattedArray[i])


def run(size, iterations, funds):
    # generate random population
    population = generatePopulation(size)
    population = sorted(
        population,
        key=lambda genome: calculateFitness(genome, funds),
        reverse=True
    )
    print("Initial fitness value: " + str(populationFitness(population, funds)))
    nextGen = population[0:2]
    for i in range(iterations):
        for j in range(int(len(population) / 2)):
            parents = selection(population, funds)
            offspring1, offspring2 = middlePointCrossover(parents)
            offspring1 = mutation(offspring1)
            offspring2 = mutation(offspring2)
            nextGen.append(offspring1)
            nextGen.append(offspring2)
        population = nextGen
        nextGen = []

    print("Finishing fitness value: " + str(populationFitness(population, funds)))
    population = sorted(
        population,
        key=lambda genome: calculateFitness(genome, funds),
        reverse=True
    )
    # formatResult(population[0], funds)
    return population[0]


print(run(150, 50, 5))
