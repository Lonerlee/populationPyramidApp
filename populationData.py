from bs4 import BeautifulSoup
import requests

def getCountryList():
  urlDefault = "https://www.populationpyramid.net/world/2023/"

  page = requests.get(urlDefault)
  soup = BeautifulSoup(page.text, 'html.parser')

  pageCountry = {}

  for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry[country.text.strip().upper()] = int(country['country'])

  return pageCountry

def getCountryID(countryName):
  list = getCountryList()
  return list[countryName.upper()]

class Population:
  apiURL = "https://www.populationpyramid.net/api/pp/"

  def __init__(self, countryID):
    self.countryID = countryID

  def getCountryData(self):
    url = self.apiURL + str(self.countryID) + "/2023/"
    r = requests.get(url)
    return r.json()

  def getWorldData(self):
    url = self.apiURL + "900/2023/"
    r = requests.get(url)
    return r.json()
