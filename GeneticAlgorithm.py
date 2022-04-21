import random
from datetime import datetime

random.seed(datetime.now())
# List of expenses of the month
# Name | Expense value | Importance from 1 to 10
expenses = [
    ['new wireless earbuds', 150, 4],
    ['new gaming chair', 600, 3],
    ['gym membership', 90, 7],
    ['internet', 110, 9],
    ['mobile phone', 60, 9],
    ['new clothes', 350, 5],
    ['takeout', 55, 2],
    ['car maintenance', 320, 4],
    ['savings', 100, 3],
]


def generatePopulation(size):
    population = []
    for i in range(size):
        generated = []
        for _ in range(len(expenses)):
            generated.append(random.randint(0, 1))
        print(f'Pob {i} ', generated)
        population.append(generated)
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
    ##print("Solution: ", solution)
    for i in range(len(solution)):
        if solution[i] == 1:
            # Our score is decided as the most value we can get, paying as little as posible and everything multiplied by 100 to make the numbers more readable
            score += (expenses[i][2] / expenses[i][1]) * 100
            totalPrice += expenses[i][1]
    #print(totalPrice, funds)
    if totalPrice > funds:
        score = 0
    return score


def selection(population, funds):
    fitnessWeights = [calculateFitness(
        population[i], funds) for i in range(len(population))]
    if (set(fitnessWeights) == {0}):
        raise ValueError("All fitness weights are 0, try again with a higher funds value.")
    return random.choices(
        population=population,
        weights=[calculateFitness(population[i], funds)
                 for i in range(len(population))],
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

    print("Finishing fitness value: " +
          str(populationFitness(population, funds)))
    population = sorted(
        population,
        key=lambda genome: calculateFitness(genome, funds),
        reverse=True
    )
    return population[0]