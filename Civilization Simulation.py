import random
import numpy as np
import matplotlib.pyplot as plt
import csv

#Starting Variables (DEFAULTS at the end of script)
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
#DO NOT CHANGE
peopleDictionary = []
genders = ['male','female']
plot_y = []
years = 1

class Person():
    def __init__(self, age):
        self.gender = random.choice(genders)
        self.age = age

def harvest():
    global foodStorage
    workers = 0
    for person in peopleDictionary:
        if person.age >= minWorkAge:
            if person.age <= maxWorkAge:
                workers += 1
    food_return = workers * foodYeild
    foodStorage += food_return
    return food_return

def reproduction():
    births = 0
    for person in peopleDictionary:
        if person.gender == 'female':
            if person.age >= minReproductionAge:
                if person.age <= maxReproductionAge:
                    if random.randint(0,5)==1:
                        peopleDictionary.append(Person(0))
                        births += 1
    return births

def death():
    deaths = 0
    for person in peopleDictionary:
        if person.age >= maxAge:
            peopleDictionary.remove(person)
            deaths += 1
    return deaths

def plague():
    deaths = 0
    for person in peopleDictionary:
        if random.randint(0,plagueDeathChance)==1:
            peopleDictionary.remove(person)
            deaths += 1
    return deaths

def year(years):
    harvestYeild = harvest()
    if showYearlyFoodYeild:
        print(f'Harvest Yeild for Year {years}: {harvestYeild}')
    reproductionYeild = reproduction()
    if showYearlyReproduction:
        print(f'Reproduction Yeild for Year {years}: {reproductionYeild}')
    deaths = death()
    if showYearlyDeath:
        print(f'Deaths for Year {years}: {deaths}')

    if plagues:
        if random.randint(0,plagueChance)==1:
            deaths = plague()
            if showPlaugeDeath:
                print(f'Plague! {deaths} people died during year {years} due to a plague!')
    
    for person in peopleDictionary:
        person.age += 1
    for person in peopleDictionary:
        foodStorage - 1
    population = len(peopleDictionary)
    if showYearlyPopulation:
        print(f'Population for year {years}:{population}')
    plot_y.append(population)
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