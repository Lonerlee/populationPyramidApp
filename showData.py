from populationData import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns

class showData:
  def __init__(self, name):
    self.name = name
    self.malePrc = 0
    self.femalePrc = 0
    self.maleTotal = 0
    self.femaleTotal = 0
    self.count = 0
    self.countryName = self.name
    self.populationGetData = Population(pageCountry[self.countryName])
    self.rawData = self.populationGetData.getCountryData()
    self.rawDataWorld = self.populationGetData.getWorldData()
    self.xd = {'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+'], 
                 'Male': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 'Female': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

  def printMale(self):
    return 'There is around ' + str(int(self.maleTotal)*1000) + ' males in ' + self.countryName.capitalize() + ' and they make approximately ' + str(self.malePrc) + '%' + ' of the population.'

  def printFemale(self):
    return 'There is around ' + str(int(self.femaleTotal)*1000) + ' females in ' + self.countryName.capitalize() + ' and they make approximately ' + str(self.femalePrc) + '%' + ' of the population.'

  def start(self):
    print(self.countryName.capitalize() + ' is approximately a ' + str(round(float(self.rawData['population'] / self.rawDataWorld['population']*100), 2)) + '%' + ' of the worlds population')

    print('Population of ' + self.countryName.capitalize() + ' is around ' + self.rawData['populationFormatted'] + ' people')

    print('Male population data:')
    print('AGE RANGE | APPROX. POPULATION')

    for maleCount in self.rawData['male']:
      print(maleCount['k'] + ' | ' + str(int(maleCount['v']*1000)))
      self.xd['Male'][self.count] = int(0-maleCount['v']*1000)
      self.maleTotal += maleCount['v']
      self.count += 1

    print('Female population data:')
    print('AGE RANGE | APPROX. POPULATION')

    self.count = 0

    for femaleCount in self.rawData['female']:
      print(femaleCount['k'] + ' | ' + str(int(femaleCount['v']*1000)))
      self.xd['Female'][self.count] = int(femaleCount['v']*1000)
      self.femaleTotal += femaleCount['v']
      self.count += 1

    self.malePrc = round(float(self.maleTotal / (self.maleTotal + self.femaleTotal) * 100), 2)
    self.femalePrc = round(float(self.femaleTotal / (self.maleTotal + self.femaleTotal) * 100), 2)

    df = pd.DataFrame(self.xd)

    plt.title("Population Pyramid Of " + self.countryName)

    x = np.array(self.xd['Age'])
    y = np.array(self.xd['Male'])

    for index, value in enumerate(y):
      plt.text(value, index, str(abs(value)), ha="right")

    plt.barh(x, y, color = "blue")

    x = np.array(self.xd['Age'])
    y = np.array(self.xd['Female'])

    for index, value in enumerate(y):
      plt.text(value, index, str(value))

    plt.barh(x, y, color = "pink")

    plt.xlabel("<--- Number Of Males | Number Of Females--->")
    plt.ylabel("Age Range")

    plt.show()
