import random
from datetime import datetime

random.seed(datetime.now())
# List of expenses of the month
# Name | Expense value | Importance from 1 to 10
expenses = [
    ['water', 60, 10],
    ['electricity', 39, 10],
    ['food', 39, 10],
    ['internet', 20, 7],
    ['mobile phone', 15, 7],
    ['new clothes', 120, 5],
    ['takeout', 50, 2],
    ['fix car', 50, 4],
    ['savings', 100, 3],
]

def generatePopulation(size):
    population = []
    for i in range(size):
        waterProb = random.randint(0, 1)
        electricityProb = random.randint(0, 1)
        foodProb = random.randint(0, 1)
        internetProb = random.randint(0, 1)
        phoneProb = random.randint(0, 1)
        clothesProb = random.randint(0, 1)
        takeoutProb = random.randint(0, 1)
        carProb = random.randint(0, 1)
        savingsProb = random.randint(0, 1)
        new = [waterProb, electricityProb, foodProb, internetProb, phoneProb, clothesProb, takeoutProb, carProb, savingsProb]
        print(f'Pob {i} ' , new)
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
            score += expenses[i][2]
            totalPrice += expenses[i][1]
    #print(totalPrice, funds)
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
    offspring1 = parents[0][0:5] + parents[1][5:9]
    offspring2 = parents[1][0:5] + parents[0][5:9]

    return offspring1, offspring2


def formatResult(array, funds):
    formattedArray = []
    print(array)
    for i in range(len(array)):
        if array[i] == 1:
            formattedArray.append(expenses[i][0])
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
    return population[0]


