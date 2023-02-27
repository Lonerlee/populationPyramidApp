from populationData import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pageCountry = getCountryList()

listShow = input('Type in Y if you want to see list of avilable or type in any word or key to not see the list - ').upper()

if listShow == 'Y':
  print(pageCountry)

countryName = input('Type in country name from the list - ').upper()

populationGetData = Population(pageCountry[countryName])

rawData = populationGetData.getCountryData()
rawDataWorld = populationGetData.getWorldData()

print(countryName.capitalize() + ' is approximately a ' + str(round(float(rawData['population'] / rawDataWorld['population']*100), 2)) + '%' + ' of the worlds population')

print('Population of ' + countryName.capitalize() + ' is around ' + rawData['populationFormatted'] + ' people')

maleTotal = 0
femaleTotal = 0

print('Male population data:')
print('AGE RANGE | APPROX. POPULATION')

for maleCount in rawData['male']:
  print(maleCount['k'] + ' | ' + str(int(maleCount['v']*1000)))
  maleTotal += maleCount['v']

print('Female population data:')
print('AGE RANGE | APPROX. POPULATION')

for femaleCount in rawData['female']:
  print(femaleCount['k'] + ' | ' + str(int(femaleCount['v']*1000)))
  femaleTotal += femaleCount['v']

malePrc = round(float(maleTotal / (maleTotal + femaleTotal) * 100), 2)
femalePrc = round(float(femaleTotal / (maleTotal + femaleTotal) * 100), 2)

print('There is around ' + str(int(maleTotal)*1000) + ' males in ' + countryName.capitalize() + ' and they make approximately ' + str(malePrc) + '%' + ' of the population')
print('There is around ' + str(int(femaleTotal)*1000) + ' females in ' + countryName.capitalize() + ' and they make approximately ' + str(femalePrc) + '%' + ' of the population')

df = pd.DataFrame({'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+'], 
                    'Male': [-49228000, -61283000, -64391000, -52437000, -42955000, -44667000, -31570000, -23887000, -22390000, -20971000, -17685000, -15450000, -13932000, -11020000, -7611000, -4653000, -1952000, -625000, -116000, -14000, -1000], 
                    'Female': [52367000, 64959000, 67161000, 55388000, 45448000, 47129000, 33436000, 26710000, 25627000, 23612000, 20075000, 16368000, 14220000, 10125000, 5984000, 3131000, 1151000, 312000, 49000, 4000, 0]})

AgeClass = ['100+','95-99','90-94','85-89','80-84','75-79','70-74','65-69','60-64','55-59','50-54','45-49','40-44','35-39','30-34','25-29','20-24','15-19','10-14','5-9','0-4']

bar_plot = sns.barplot(x='Male', y='Age', data=df, order=AgeClass)

bar_plot = sns.barplot(x='Female', y='Age', data=df, order=AgeClass)

bar_plot.set(xlabel="Population (hundreds of millions)", ylabel="Age-Group", title = "Population Pyramid")

plt.show()
