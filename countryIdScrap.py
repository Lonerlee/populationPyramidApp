from bs4 import BeautifulSoup
import requests

urlDefault = "https://www.populationpyramid.net/world/2023/"

page = requests.get(urlDefault)
soup = BeautifulSoup(page.text, 'html.parser')

pageCountry = {0: 'id'}

for country in soup.find_all('a', {'class':"countryLink"}):
    pageCountry[int(country['country'])] = country.text.strip()

print(pageCountry)
