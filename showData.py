from populationData import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class showData:
  numbersData = {'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+'], 
                 'Male': [], 
                 'Female': []}
  pageCountry = getCountryList()

  def __init__(self, countryName):
    self.countryName = countryName

  def printMale(self):
    return 'There is around ' + str(int(-(sum(self.numbersData['Male'])))) + ' males in ' + self.countryName.capitalize() + ' and they make approximately ' + str(round(float((abs(sum(self.numbersData['Male']))) / ((abs(sum(self.numbersData['Male']))) + sum(self.numbersData['Female'])) * 100), 2)) + '%' + ' of the population.'

  def printFemale(self):
    return 'There is around ' + str(int(sum(self.numbersData['Female']))) + ' females in ' + self.countryName.capitalize() + ' and they make approximately ' + str(round(float((sum(self.numbersData['Female'])) / ((abs(sum(self.numbersData['Male']))) + (sum(self.numbersData['Female']))) * 100), 2)) + '%' + ' of the population.'

  def printWorld(self):
    return self.countryName.capitalize() + ' is approximately a ' + str(round(float(Population(self.pageCountry[self.countryName]).getCountryData()['population'] / Population(self.pageCountry[self.countryName]).getWorldData()['population']*100), 2)) + '%' + ' of the worlds population'

  def calculations(self):
    self.numbersData['Female'].clear()
    for femaleCount in Population(self.pageCountry[self.countryName]).getCountryData()['female']:
      self.numbersData['Female'].append(int(femaleCount['v']*1000))

    self.numbersData['Male'].clear()
    for maleCount in Population(self.pageCountry[self.countryName]).getCountryData()['male']:
      self.numbersData['Male'].append(int(-maleCount['v']*1000))

  def start(self):
    self.calculations()

    df = pd.DataFrame(self.numbersData)

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
