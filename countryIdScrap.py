from bs4 import BeautifulSoup
import requests
import pprint

urlDefault = "https://www.populationpyramid.net/world/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

headers = ['ID', 'Country']

pageCountry = {}

for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry[country.text.strip().upper()] = int(country['country'])

listShow = 'N'

listShow = input('Type in Y if you want to see list of avilable - ').upper()

if listShow == 'Y':
  print(headers)
  pprint.pprint(pageCountry)

countryID = pageCountry[input('Type in country name from the list - ').upper()]

urlDefault = "https://www.populationpyramid.net/" + str(countryID) + "/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

countryData = {}

print('Approximate number of this country population is - ' + soup.find('span', {'class':"population-number"}).text.strip())