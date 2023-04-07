import random
import numpy as np
import matplotlib.pyplot as plt
import csv

#Starting Variables (DEFAULTS at the end of script)
startingPop = 500
yearLimit = 200
foodYeild = 1
foodStorage = 0
startingFood = 0
minWorkAge = 8
maxWorkAge = 80
minReproductionAge = 18
maxReproductionAge = 35
minDeathAge = 60
maxDeathAge = 85
plagues = True
plagueChance = 20
plagueDeathChance = 20
#Visual Numbers
showYearlyPopulation = False
showYearlyFoodYeild = False
showYearlyReproduction = False
showYearlyDeath = False
showPlaugeDeath = False
pauseYearlyCycle = False
#DO NOT CHANGE
peopleDictionary = []
GENDERS = ['male','female']
plot_y = []
years = 1

#Person Template
class Person():
    def __init__(self, age):
        self.gender = random.choice(GENDERS)
        self.age = age

#Harvests food for each worker every year cycle
def harvest():
    global foodStorage
    workers = len([p for p in peopleDictionary if minWorkAge <= p.age <= maxWorkAge])
    food_return = workers * foodYeild
    foodStorage += food_return
    return food_return


#Adds to the population
def reproduction():
    births = len([p for p in peopleDictionary if p.gender == 'female' if minReproductionAge <= p.age <= maxReproductionAge if random.randint(0,5)==1])
    for i in range(births):
        peopleDictionary.append(Person(0))
    return births

#Kills older ages
def death():
    deaths = 0
    for person in peopleDictionary:
        if person.age >= random.randint(minDeathAge,maxDeathAge):
            peopleDictionary.remove(person)
            deaths += 1
    return deaths

#Randomly has a chance of killing people in a plague
def plague():
    deaths = 0
    for person in peopleDictionary:
        if random.randint(0,plagueDeathChance)==1:
            peopleDictionary.remove(person)
            deaths += 1
    return deaths

#Runs a year cycle
def year(years):
    #Runs a harvest
    harvestYeild = harvest()
    if showYearlyFoodYeild:
        print(f'Harvest Yeild for Year {years}: {harvestYeild}')

    #Runs reproduction
    reproductionYeild = reproduction()
    if showYearlyReproduction:
        print(f'Reproduction Yeild for Year {years}: {reproductionYeild}')
    
    #Runs death
    deaths = death()
    if showYearlyDeath:
        print(f'Deaths for Year {years}: {deaths}')

    #Runs plauge event if enabled
    if plagues:
        if random.randint(0,plagueChance)==1:
            deaths = plague()
            if showPlaugeDeath:
                print(f'Plague! {deaths} people died during year {years} due to a plague!')

    #Ages everyone a year
    ages = np.array([person.age for person in peopleDictionary])
    np.add(ages, 1, out=ages)

    #Gets the current population and stores it
    population = len(peopleDictionary)
    if showYearlyPopulation:
        print(f'Population for year {years}:{population}')
    plot_y.append(population)

    #Executes if sim is over
    if years >= yearLimit:
        print('Simulation Done!')
        x=range(0,years)
        #Creates Plot
        plt.title("Population in Human Simulation")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.fill_between(x, plot_y)
        plt.show()
        exit()
    years += 1
    if pauseYearlyCycle:
        input('Press ENTER to continue... ')
    year(years)

#Setups the sim
def beginSim():
    foodStorage = startingFood
    for x in range(startingPop):
        peopleDictionary.append(Person(random.randint(18,50)))
    print("Starting Simulation...")
    year(years)
beginSim()

#DEFAULT Variables for Starting Variables
'''
startingPop = 50
yearLimit = 350
foodYeild = 1
foodStorage = 0
startingFood = 0
minWorkAge = 8
maxWorkAge = 80
minReproductionAge = 18
maxReproductionAge = 35
maxAge = 85
plagues = True
plagueChance = 20
plagueDeathChance = 20
#Visual Numbers
showYearlyPopulation = False
showYearlyFoodYeild = False
showYearlyReproduction = False
showYearlyDeath = False
showPlaugeDeath = True
pauseYearlyCycle = False
'''