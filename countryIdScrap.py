from bs4 import BeautifulSoup
import requests

urlDefault = "https://www.populationpyramid.net/world/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

pageCountry = []
for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry.append(country.text.strip())
    pageCountry.append(country['country'])

print(pageCountry)
