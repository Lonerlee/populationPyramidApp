from bs4 import BeautifulSoup
import json
import requests
import tkinter as tk
import pprint

urlDefault = "https://www.populationpyramid.net/world/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

pageCountry = {}

for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry[country.text.strip().upper()] = int(country['country'])

listShow = input('Type in Y if you want to see list of avilable or type in any word or key to not see the list - ').upper()

if listShow == 'Y':
  pprint.pprint(pageCountry)

countryName = input('Type in country name from the list - ').upper()

countryID = pageCountry[countryName]

jsonDataURL = "https://www.populationpyramid.net/api/pp/" + str(countryID) + "/2023/"
jsonWorldData = "https://www.populationpyramid.net/api/pp/900/2023/"

r = requests.get(jsonDataURL)
rW = requests.get(jsonWorldData)

rawData = r.json()
rawDataWorld = rW.json()

print(countryName.capitalize() + ' is approximately a ' + str(round(float(rawData['population'] / rawDataWorld['population']*100), 2)) + '%' + ' of the worlds population')

print('Population of ' + countryName.capitalize() + ' is around ' + rawData['populationFormatted'] + ' people')

maleTotal = 0
femaleTotal = 0

maleInt = 0
femaleInt = 0

print('Male population data:')
print('AGE RANGE | APPROX. POPULATION')

for x in rawData['male']:
  print(rawData['male'][maleInt]['k'] + ' | ' + str(int(rawData['male'][maleInt]['v']*1000)))
  maleTotal += rawData['male'][maleInt]['v']
  maleInt += 1

print('Female population data:')
print('AGE RANGE | APPROX. POPULATION')

for x in rawData['female']:
  print(rawData['female'][femaleInt]['k'] + ' | ' + str(int(rawData['female'][femaleInt]['v']*1000)))
  femaleTotal += rawData['female'][femaleInt]['v']
  femaleInt += 1

malePrc = round(float(maleTotal / (maleTotal + femaleTotal) * 100), 2)
femalePrc = round(float(femaleTotal / (maleTotal + femaleTotal) * 100), 2)

print('There is around ' + str(int(maleTotal)*1000) + ' males in ' + countryName.capitalize() + ' and they make approximately ' + str(malePrc) + '%' + ' of the population')
print('There is around ' + str(int(femaleTotal)*1000) + ' females in ' + countryName.capitalize() + ' and they make approximately ' + str(femalePrc) + '%' + ' of the population')