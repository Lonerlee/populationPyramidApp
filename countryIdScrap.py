from bs4 import BeautifulSoup
import json
import requests
import pprint

urlDefault = "https://www.populationpyramid.net/world/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

pageCountry = {}

for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry[country.text.strip().upper()] = int(country['country'])

listShow = input('Type in Y if you want to see list of avilable or type in anything to not see the list - ').upper()

if listShow == 'Y':
  pprint.pprint(pageCountry)

countryName = input('Type in country name from the list - ').upper()

countryID = pageCountry[countryName]

jsonDataURL = "https://www.populationpyramid.net/api/pp/" + str(countryID) + "/2023/"

r = requests.get(jsonDataURL)

rawData = r.json()

print('Population of ' + countryName + ' is around ' + rawData['populationFormatted'])
print('Male population data:')
maleInt = 0
print('AGE RANGE / APPROXIMATE POPULATION')

for x in rawData['male']:
  print(rawData['male'][maleInt]['k'] + '   /   ' + str(int(rawData['male'][maleInt]['v']*1000)))
  maleInt += 1

print('Female population data:')
print('AGE RANGE / APPROXIMATE POPULATION')
femaleInt = 0

for x in rawData['female']:
  print(rawData['female'][femaleInt]['k'] + '   /   ' + str(int(rawData['female'][femaleInt]['v']*1000)))
  femaleInt += 1
