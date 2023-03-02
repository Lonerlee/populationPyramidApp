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

xd = {'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+'], 
                    'Male': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    'Female': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

maleTotal = 0
femaleTotal = 0

count = 0

print('Male population data:')
print('AGE RANGE | APPROX. POPULATION')

for maleCount in rawData['male']:
  print(str(maleCount) + ' ' + maleCount['k'] + ' | ' + str(int(maleCount['v']*1000)))
  xd['Male'][count] = int(maleCount['v']*1000)
  maleTotal += maleCount['v']
  count += 1

print('Female population data:')
print('AGE RANGE | APPROX. POPULATION')

count = 0

for femaleCount in rawData['female']:
  print(femaleCount['k'] + ' | ' + str(int(femaleCount['v']*1000)))
  xd['Female'][count] = int(femaleCount['v']*1000)
  femaleTotal += femaleCount['v']
  count += 1

malePrc = round(float(maleTotal / (maleTotal + femaleTotal) * 100), 2)
femalePrc = round(float(femaleTotal / (maleTotal + femaleTotal) * 100), 2)

print('There is around ' + str(int(maleTotal)*1000) + ' males in ' + countryName.capitalize() + ' and they make approximately ' + str(malePrc) + '%' + ' of the population')
print('There is around ' + str(int(femaleTotal)*1000) + ' females in ' + countryName.capitalize() + ' and they make approximately ' + str(femalePrc) + '%' + ' of the population')

df = pd.DataFrame(xd)

y = range(0, len(df))
x_male = df['Male']
x_female = df['Female']

fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))

fig.patch.set_facecolor('xkcd:silver')
plt.figtext(.5,.94,"Population Pyramid of " + countryName.capitalize(), fontsize=15, ha='center')

axes[0].barh(y, x_male, align='center', color='mediumblue')
axes[0].set(title='Males')
axes[1].barh(y, x_female, align='center', color='fuchsia')
axes[1].set(title='Females')

axes[1].grid()
axes[0].set(yticks=y, yticklabels=df['Age'])
axes[0].invert_xaxis()
axes[0].grid()

plt.show()
