from populationData import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class showData:
  numbersData = {'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+'], 
                 'Male': [], 
                 'Female': []}

  def __init__(self, countryName, countryList):
    self.countryName = countryName
    self.pageCountry = countryList
    self.population = Population(self.pageCountry[self.countryName])
    self.data = self.population.getCountryData()

  def getGenderQuantity(self, gender):
    allQuantity = 0
    for x in self.data[gender]:
      ageQuantity = round(x['v']*1000)
      allQuantity +=ageQuantity
    return allQuantity
  
  def printMale(self):
    numberOfMales = self.getGenderQuantity('male')
    percentageOfMales = str(round((100 * numberOfMales/(self.data['population']*1000)), 2))
    return 'Number of males is ' + str(numberOfMales) + ' in ' + self.countryName.capitalize() + ' and makes approx. ' + percentageOfMales + '%' + ' of the population.'

  def printFemale(self):
    numberOfFemales = self.getGenderQuantity('female')
    percentageOfFemales = str(round((100 * numberOfFemales/(self.data['population']*1000)), 2))
    return 'Number of females is ' + str(numberOfFemales) + ' in ' + self.countryName.capitalize() + ' and makes approx. ' + percentageOfFemales + '%' + ' of the population.'

  def printWorld(self):
    fractionPopulation = str(round(float(self.data['population'] / self.population.getWorldData()['population']*100), 2))
    return self.countryName.capitalize() + ' is approximately a ' + fractionPopulation + '%' + ' of the worlds population'

  def insertData(self):
    self.numbersData['Female'].clear()
    for femaleCount in self.data['female']:
      self.numbersData['Female'].append(int(femaleCount['v']*1000))

    self.numbersData['Male'].clear()
    for maleCount in self.data['male']:
      self.numbersData['Male'].append(int(-maleCount['v']*1000))

  def start(self):
    self.insertData()

    df = pd.DataFrame(self.numbersData)

    plt.close('all')

    plt.title("Population Pyramid Of " + self.countryName)

    x = np.array(self.numbersData['Age'])
    y = np.array(self.numbersData['Male'])

    for index, value in enumerate(y):
      plt.text(value, index, str(abs(value)), ha="right")

    plt.barh(x, y, color = "blue")

    x = np.array(self.numbersData['Age'])
    y = np.array(self.numbersData['Female'])

    for index, value in enumerate(y):
      plt.text(value, index, str(value))

    plt.barh(x, y, color = "pink")

    plt.xlabel("<--- Number Of Males | Number Of Females--->")
    plt.ylabel("Age Range")

    plt.show()
